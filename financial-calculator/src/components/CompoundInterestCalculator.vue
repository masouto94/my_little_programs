<template>
    <div class="formContainer">
        <form action="">
            <input type="number" name="amount" id="" v-model="amount">
            <input type="number" name="interest" id="" v-model="interest">
            <input type="date" name="from" id="" v-model="from">
            <input type="date" name="to" id="" v-model="to">
            <input type="button" :value="$t('buttons.calculate')" v-on:click="handleCalculateCompuondInterest">
        </form>
        <div class="inflationContainer">
            <span>Total</span>
            <span v-if="this.from && this.to">{{ accumulated }}</span>
        </div>
    </div> 
</template>

<script>
import {calculateCompuondInterest} from '../utils/calculators'
export default {
    name: 'CompoundInterestCalculator',
    data() {
        return {
            amount:100,
            interest:10,
            from: '2022-05-01',
            to: '2022-06-01',
            accumulated: undefined
        }
    },
    methods: {
        handleCalculateCompuondInterest(){
            this.accumulated = calculateCompuondInterest(this.amount,this.interest,this.from,this.to)
        }
    },
    computed: {
    },
    mounted() {
  }
        

}
</script>

<style scoped>

</style>