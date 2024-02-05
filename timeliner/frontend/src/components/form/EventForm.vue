<template>
    <form  action="/dataentry" @submit="sendData" method="post">
        <EventInput v-for="i in 5" :key="i" @input="(e) => check(e,i-1)"/>
      </form>
</template>

<script>
import axios from 'axios'
import EventInput from './EventInput.vue'
export default {
    name: 'EventForm',
    components:{
        EventInput
    },
    data() {
        return {
            timelineData:{
                
            }
        } 
    },
    methods: {
        sendData: function (e) {
          e.preventDefault()
            const path = `http://127.0.0.1:5000/dataentry`
            console.log(path)
            axios.post(path, {
                name: this.timeLineData.dates,
                department: this.timeLineData.episodes,
            }
            )
                .then(response => {
                    console.log(response);
                })
                .catch(err => { console.log(err);
                });
        },
        check: function(e,index){
            if(!this.timelineData[index]){
                this.timelineData[index] = {
                        [e.target["name"]]: e.target.value
                    }
            }
            this.timelineData[index][e.target["name"]] = e.target.value
            console.log(JSON.stringify(this.timelineData))

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