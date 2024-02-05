<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <CreateTimeline/>
</template>

<script>
import CreateTimeline from './views/CreateTimeline.vue'

export default {
  name: 'App',
  components: {
    CreateTimeline
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
