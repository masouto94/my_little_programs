<template>
        <div id="formContainer">
            <form action="">
                <input type="month" name="month" id="monthPicker" :min="minDate" :max="maxDate" v-model="selected" v-on:change="handleClear">
                <input type="button" value="search" v-on:click="show">
            </form>
            <div id="inflationContainer">
                {{ $t("body.calculatorLegend") }}
                <span v-if="this.selected">{{percInflation}}</span>
            </div>
        </div>

</template>
<script>
import { inflationSeries } from '../data/data.js'
import {isEmpty} from '../utils/stringUtils.js'
export default {
    name: 'CalculatorInput',
    data() {
        return {
            inflation: inflationSeries,
            selected: null,
            percInflation: undefined,

        }
    },
    methods: {
        isEmpty,
        handleClear: function(){
            if(isEmpty(this.selected)){
                this.selected = null
                this.percInflation = undefined
                return
            }
            this.percInflation = undefined
        },
        validateForm: function(){
            if(isEmpty(this.selected)){
                alert("Select a date")
                return false
            }
            return true
        },
        parseDate: function (toParse) {
            const splitted = toParse.split("-")
            return [parseInt(splitted[0]), parseInt(splitted[1])]
        },
        show: function () {
            if(this.validateForm()){
                const [year, month] = this.parseDate(this.selected)
                const registry = this.inflation.find((values) => values.year === year && values.month === month)
                this.percInflation = registry.amount
            }
        }
    },
    computed: {
        minDate: {
            get: function () {
                let {year, month} = this.inflation[0]
                let parsedMonth = month < 10 ? "0" + month.toString() : month.toString()
                return year.toString() + "-" + parsedMonth
            }
        },
        maxDate: {
            get: function () {
                let {year, month} = this.inflation.slice(-1)[0]
                let parsedMonth = month < 10 ? "0" + month.toString() : month.toString()
                return year.toString() + "-" + parsedMonth
            }
        }
    },
    mounted() {
        this.selected = this.maxDate
  }
        

}
</script>
<style scoped>
h1 {
    color: blue;
}

#formContainer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
#inflationContainer{
    display: grid;
    grid-template-columns: 1fr 1fr;
    max-width: 20%;
    align-items: center;

}
</style>