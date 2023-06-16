<template>
    <div class="togglerBarContainer">

    <div class="togglerBar second-color">
        <button class="togglerButton third-color" @click="toggle" label="month">{{ $t("buttons.monthly")}}</button>
        <button class="togglerButton third-color" @click="toggle" label="cumulative">{{ $t("buttons.cumulative")}}</button>
        <button class="togglerButton third-color" @click="toggle" label="interest">{{ $t("buttons.interest")}}</button>

    </div>

<div class="spoilers second-color">
    <v-spoiler v-model="showMonth" style="--spoiler-time: 150ms;">
        <CalculatorInput/>
    </v-spoiler>
    <v-spoiler v-model="showCumulative" style="--spoiler-time: 150ms;">
        <CumulativeForm/>
    </v-spoiler>
    <v-spoiler v-model="showInterest" style="--spoiler-time: 150ms;">
        <CompoundInterestCalculator/>
    </v-spoiler>
</div>
</div>
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
            showInterest: false,
        }
    },
    methods: {
        toggle: function(e){
            const labeled = e.target.getAttribute("label")
            e.target.classList.toggle("selected")
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

.selected{
    border-style: inset ;
    color: white;
}

.formContainer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.togglerButton{
    margin: 1%;
    border-radius: 25%;
    height:3rem;
    border-style: outset;
    min-width: 100px;    
}

.togglerBarContainer{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    
}
.spoilers{
    width: 50%;
}
.togglerBar{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 50%;
    border-radius: 25px 25px 0px 0px;
    height: 10vh;
    align-items: center;
}
</style>