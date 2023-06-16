<template>
    <div class="formContainer">
        <form action="">
            <input type="month" name="month" id="monthPicker" :min="minDate" :max="maxDate" v-model="selected"
                v-on:change="handleClear">
            <input type="button"  :value="$t('buttons.search')" v-on:click="displayInflation">
        </form>
        <div class="inflationContainer">
            <span>{{ $t("body.monthCalculatorLegend") }}</span>
            <span v-if="this.selected">{{ percInflation }}</span>
        </div>
    </div>
</template>
<script>
import { inflationSeries } from '../data/data.js'
import { isEmpty, parseDate } from '../utils/stringUtils.js'
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
        parseDate,
        handleClear: function () {
            if (isEmpty(this.selected)) {
                this.selected = null
                this.percInflation = undefined
                return
            }
            this.percInflation = undefined
        },
        validateDate: function (date) {
            try {
                const [year, month] = parseDate(date)
                const [minYear, minMonth] = parseDate(this.minDate)
                const [maxYear, maxMonth] = parseDate(this.maxDate)
                const asDate = new Date(year, month - 1)
                const minDateAsDate = new Date(minYear, minMonth - 1)
                const maxDateAsDate = new Date(maxYear, maxMonth - 1)
                const valid = (asDate.getTime() >= minDateAsDate.getTime()) && (asDate.getTime() <= maxDateAsDate.getTime())
                return valid
            } catch (error) {
                return false
            }
        },
        validateForm: function () {
            if (isEmpty(this.selected)) {
                alert(this.$t("errors.validDate"))
                return false
            }
            if (!this.validateDate(this.selected)) {
                alert(`${this.$t("errors.validDateInterval", { minDate: this.minDate, maxDate: this.maxDate })}`)
                return false
            }

            return true
        },
        displayInflation: function () {
            if (this.validateForm()) {
                const [year, month] = parseDate(this.selected)
                const registry = this.inflation.find((values) => values.year === year && values.month === month)
                this.percInflation = registry.amount
            }
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
        this.selected = this.maxDate
    }


}
</script>
<style scoped>
h1 {
    color: blue;
}



</style>