<template>
    <form action="/dataentry"  method="post">

        <div class="previous" v-for="(applicant, counter) in inputList" v-bind:key="counter">
            <EventInput @input="(e) => check(e, counter)" />
            <button @click="(e) => deleteInput(e,counter)">-</button>
            <button @click="addInput">+</button>
        </div>
    </form>
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
                .catch(err => {
                    console.log(err);
                });
        },
        check: function (e, index) {
            // if (!this.inputList[index]) {
            //     this.inputList[index] = {
            //         [e.target["name"]]: e.target.value
            //     }
            // }
            this.inputList[index][e.target["name"]] = e.target.value
            console.log(JSON.stringify(this.inputList))

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
        }
    },
    computed: {
    },
    mounted() {
    }


}
</script>

<style scoped></style>