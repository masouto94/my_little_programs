<template>
  <div class="timeline">
    <h1>TIMELINE</h1>
    <EventForm/>
  </div>
</template>

<script>
import EventForm from '../components/form/EventForm.vue'
export default {
  name: 'CreateTimeline',
  components:{
    EventForm
  },
  data() {
        return{

        };
    },
    methods: {
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
