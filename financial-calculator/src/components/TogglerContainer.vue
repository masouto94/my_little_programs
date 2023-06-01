<template>
    <div>
        <button @click="toggle" label="month">{{ $t("buttons.monthly")}}</button>
        <button @click="toggle" label="cumulative">{{ $t("buttons.cumulative")}}</button>
        <button @click="toggle" label="interest">{{ $t("buttons.interest")}}</button>

    </div>
    <v-spoiler v-model="showMonth" style="--spoiler-time: 150ms;">
        <CalculatorInput/>
    </v-spoiler>
    <v-spoiler v-model="showCumulative" style="--spoiler-time: 150ms;">
        <CumulativeForm/>
    </v-spoiler>
    <v-spoiler v-model="showInterest" style="--spoiler-time: 150ms;">
        <CompoundInterestCalculator/>
    </v-spoiler>
</template>

<script>
import VSpoiler from 'v-spoiler';
import 'v-spoiler/dist/v-spoiler.css';
import CalculatorInput from './CalculatorInput.vue'
import CumulativeForm from './CumulativeForm.vue'
import CompoundInterestCalculator from './CompoundInterestCalculator.vue';

export default {
    name: 'TogglerContainer',
    components:{
        CalculatorInput,
        CumulativeForm,
        CompoundInterestCalculator,
        VSpoiler
    },
    data() {
        return {
            showMonth: false,
            showCumulative: false,
            showInterest: true
        }
    },
    methods: {
        toggle: function(e){
            const labeled = e.target.getAttribute("label")
            switch (true) {
                case labeled === "month":
                    this.showMonth = !this.showMonth
                    break;
                case labeled === "cumulative":
                    this.showCumulative = !this.showCumulative
                    break;
                case labeled === "interest":
                    this.showInterest = !this.showInterest
                    break;           
                default:
                    break;
            }
        }
    },
    computed: {
    },
    mounted() {
  }
        

}
</script>

<style >
.inflationContainer {
    display: grid;
    grid-template-columns: 1fr 1fr;
    max-width: 20%;
    align-items: center;

}

.formContainer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>