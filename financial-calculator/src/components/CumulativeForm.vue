<template>
    <div class="formContainer">
        <form action="">
            <input type="month" name="from" :min="minDate" :max="maxDate" id="" v-on:change="handleClear('from')" v-model="from">
            <input type="month" name="to" :min="minDate" :max="maxDate" id="" v-on:change="handleClear('to')" v-model="to">
            <input type="button" :value="$t('buttons.calculate')" v-on:click="showInflation">
        </form>
        <div class="inflationContainer">
            <span>{{ $t("body.intervalCalculatorLegend") }}</span>
            <span v-if="this.from && this.to">{{ accumulated }}</span>
        </div>
    </div> 
</template>

<script>
import { inflationSeries } from '../data/data.js'
import { isEmpty, parseDate } from '../utils/stringUtils.js'

export default {
    name: 'CumulativeForm',
    data() {
        return {
            inflation: inflationSeries,
            from: undefined,
            to: undefined,
            accumulated: undefined
        }
    },
    methods: {
        handleClear: function (item) {
            if (isEmpty(this[item])) {
                this[item] = null
                this.accumulated = undefined
                return
            }
            this.accumulated = undefined
        },
        calculateInflation: function(from,to){
            if(from.index === to.index){
                return to.amount
            }
            const filteredInflation = this.inflation.filter((item) => item.index >= from.index && item.index <= to.index)
            const cumulative = filteredInflation.reduce(
            (accumulator, currentValue) => accumulator + currentValue.amount,0);
            return (cumulative).toFixed(2)
        },
        showInflation: function(){
            const [initialYear, initialMonth] = parseDate(this.from)
            const [finalYear, finalMonth] = parseDate(this.to)
            const initialRegistry = this.inflation.find((values) => values.year === initialYear && values.month === initialMonth)
            const finalRegistry = this.inflation.find((values) => values.year === finalYear && values.month === finalMonth)
            this.accumulated = this.calculateInflation(initialRegistry, finalRegistry)

        }
    },
    computed: {
        minDate: {
            get: function () {
                let { year, month } = this.inflation[0]
                let parsedMonth = month < 10 ? "0" + month.toString() : month.toString()
                return year.toString() + "-" + parsedMonth
            }
        },
        maxDate: {
            get: function () {
                let { year, month } = this.inflation.slice(-1)[0]
                let parsedMonth = month < 10 ? "0" + month.toString() : month.toString()
                return year.toString() + "-" + parsedMonth
            }
        }
    },
    mounted() {
        this.from = this.minDate
        this.to = this.maxDate

  }
        

}
</script>

<style scoped>

</style>