<template>
    <div class="formContainer">
        <span v-if="this.span !== this.$t('selector.yearly')" class="disclaimer">
            <i>{{$t('body.calculatorDisclaimer')}}</i>
        </span>
        <form action="">
            <input type="number" name="amount" id="" v-model="amount" :placeholder="$t('inputs.amount')">
            <input type="number" name="interest" id="" v-model="interest" :placeholder="$t('inputs.interest')">
            <select v-model="span">
                <option>{{ $t('selector.daily') }}</option>
                <option>{{ $t('selector.monthly') }}</option>
                <option>{{ $t('selector.yearly') }}</option>
              </select>
            <input type="number" name="repetitions" id="" v-model="repetitions" :placeholder="$t('inputs.repetitions')">
            <input  type="button" :value="$t('buttons.calculate')" @click="handleCalculateCompoundInterest">
        </form>
        <div class="inflationContainer">
            <span>Total</span>
            <span v-if="this.accumulated">{{ accumulated }}</span>
        </div>
    </div> 
</template>

<script>
import {calculateCompoundInterest} from '../utils/calculators'
export default {
    name: 'CompoundInterestCalculator',
    data() {
        return {
            amount: undefined,
            interest: undefined,
            repetitions: undefined,
            accumulated: undefined,
            span: this.$t('selector.yearly')
        }
    },
    methods: {
       handleCalculateCompoundInterest: function(){
            
            if(this.validateInput()){
                this.accumulated = calculateCompoundInterest(this.amount,this.interest,this.interval, this.repetitions)
            }
        },
        validateInput: function(){
            if(this.amount && this.interest && this.repetitions){
                return true
            }
            alert(this.$t('errors.calculatorInput'))
            return false
        }
    },
    computed: {
        interval:{
            get: function(){
                switch (this.span) {
                    case this.$t('selector.daily'):
                        return 1
                    case this.$t('selector.monthly'):
                        return 30
                    case this.$t('selector.yearly'):
                        return 365
                    default:
                        alert(this.$t("errors.validDate"))
                        return undefined
                }
            }
        }
    },
    mounted() {
  }
        

}
</script>

<style scoped>
input[type="number"] {
    width: 6vw;
}

.disclaimer{
    font-size: 0.8rem;

}


</style>