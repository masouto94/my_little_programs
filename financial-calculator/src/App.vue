<template>
  <BasicHeader />
  <TogglerContainer/>
</template>

<script>
import BasicHeader from './components/BasicHeader.vue';
import TogglerContainer from './components/TogglerContainer.vue';

export default {
  name: 'App',
  components: {
    BasicHeader,
    TogglerContainer
},
  data(){
    return{
      
    }
  }
}
</script>

<style src="./utils/colors.css"></style>
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
