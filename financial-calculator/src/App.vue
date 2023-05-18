<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <TestingVue :date="now" />
</template>

<script>
import TestingVue from './components/TestingVue.vue'

export default {
  name: 'App',
  components: {
    TestingVue
  },
  data(){
    return{
      now: new Date()
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
