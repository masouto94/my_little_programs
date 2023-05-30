<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <CalculatorInput />
</template>

<script>
import CalculatorInput from './components/CalculatorInput.vue'

export default {
  name: 'App',
  components: {
    CalculatorInput
  },
  data(){
    return{
      
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
