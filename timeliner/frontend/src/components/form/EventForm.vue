<template>
    <form action="/dataentry" @submit.stop.prevent="sendData"  method="post">

        <div class="previous" v-for="(data, counter) in inputList" v-bind:key="counter">
            <EventInput 
            @input="(e) => updateInputData(e, counter)"
            :date="inputList[counter].date"
            :episode="inputList[counter].episode" 
            />
        </div>
        <input type="submit" value="MANDAR">
    </form>
    <div>
        <button type="reset" @click="resetForm">RESET</button>
    </div>
    <div id="chartContainer">

    </div>
</template>

<script>
import axios from 'axios'
import EventInput from './EventInput.vue'
export default {
    name: 'EventForm',
    components: {
        EventInput
    },
    data() {
        return {
            
            inputList: [
                {
                    date: "",
                    episode: ""
                }
            ]
        }
    },
    methods: {
        sendData: async function  (e) {
            e
            // alert(JSON.stringify(this.inputList))
            const path = `http://127.0.0.1:5000/dataentry`
            const data = await axios.post(path, this.inputList)
            .then(response => {
                return response.data
            })
            .catch(err => {
                console.log(err);
            });
            const container = document.querySelector("#chartContainer")
            container.innerHTML  = data
        },
        updateInputData: function (e, index) {
            this.inputList[index][e.target["name"]] = e.target.value
            localStorage.setItem('timelineData',JSON.stringify(this.inputList))
            console.log(localStorage.getItem('timelineData'))

        },
        addInput(e) {
            e.preventDefault()
            this.inputList.push({
                    date: "",
                    episode: ""
                })
        },
        deleteInput(e,counter) {
            e.preventDefault()
            this.inputList.splice(counter, 1);
        },
        resetForm(e) {
            e.preventDefault()
            this.inputList = [
                {
                    date: "",
                    episode: ""
                }
            ]
            localStorage.clear()
        }
    },
    computed: {
    },
    mounted() {
        if(localStorage.getItem('timelineData')){
            this.inputList = JSON.parse(localStorage.getItem('timelineData'))
        }
    },
    provide(){
        return{
            addInput:this.addInput,
            deleteInput:this.deleteInput

        }
    }


}
</script>

<style scoped>
#chartContainer {
    display: flex;
    justify-content: center;
}
</style>