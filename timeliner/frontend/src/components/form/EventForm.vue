<template>
    <form action="/createTimeline" @submit.stop.prevent="sendData"  method="post">

        <div class="previous" v-for="(data, counter) in inputList" v-bind:key="counter">
            <EventInput 
            @change="(e) => updateInputData(e, counter)"
            :from_date="inputList[counter].from_date"
            :to_date="inputList[counter].to_date || inputList[counter].from_date"
            :episode="inputList[counter].episode" 
            />
        </div>
        <input type="submit" value="MANDAR">
    </form>
    <div>
        <button type="reset" @click="resetForm">RESET</button>
    </div>
    <div class="table-responsive-md" id="chartContainer">

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
                    from_date: "",
                    to_date: "",
                    episode: ""
                }
            ]
        }
    },
    methods: {
        sendData: async function  (e) {
            e
            // alert(JSON.stringify(this.inputList))
            const path = `http://127.0.0.1:5000/createTimeline`
            const data = await axios.post(path, this.inputList)
            .then(response => {
                return response.data
            })
            .catch(err => {
                console.log(err);
            });
            console.log(localStorage.getItem('timelineData'))

            const container = document.querySelector("#chartContainer")
            container.innerHTML  = data
        },
        updateInputData: function (e, index) {
            this.inputList[index][e.target["name"]] = e.target.value
            if(!this.inputList[index]["to_date"]){
                this.inputList[index]["to_date"] = e.target.value
            }
            localStorage.setItem('timelineData',JSON.stringify(this.inputList))
            console.log(localStorage.getItem('timelineData'))

        },
        addInput(e) {
            e.preventDefault()
            this.inputList.push({
                    from_date: "",
                    to_date:"",
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
                    from_date: "",
                    to_date:"",
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