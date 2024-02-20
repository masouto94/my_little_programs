<template>
    <form>

        <div class="previous" v-for="(data, counter) in inputList" v-bind:key="counter">
            <EventInput @change="(e) => updateInputData(e, counter)" :from_date="inputList[counter].from_date"
                :to_date="inputList[counter].to_date || inputList[counter].from_date"
                :episode="inputList[counter].episode" />
        </div>
    </form>
    <div>
        <button type="submit" @click="createTable">Crear tabla</button>
        <button type="submit" @click="createChart">Crear chart</button>
        <button type="reset" @click="resetForm">RESET</button>
    </div>
    <div class="table-responsive-md container" id="tableContainer">

    </div>
    <div class="container" id="chartContainer">
        <iframe src="" frameborder="0"></iframe>
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
        createTable: async function () {
            
            const path = `${process.env.VUE_APP_API}/createTimelineTable`
            const data = await axios.post(path, this.inputList)
                .then(response => {
                    return response.data
                })
                .catch(err => {
                    console.log(err);
                });

            const container = document.querySelector("#tableContainer")
            container.innerHTML = data
        },
        createChart: async function () {
            const path = `${process.env.VUE_APP_API}/createTimelineChart`
            const data = await axios.post(path, this.inputList)
                .then(response => {
                    console.log(response)
                    return response.data
                })
                .catch(err => {
                    console.log(err);
                });

            const container = document.querySelector("#chartContainer > iframe")
            container.setAttribute('src',data)
        },
        updateInputData: function (e, index) {
            this.inputList[index][e.target["name"]] = e.target.value
            if (!this.inputList[index]["to_date"]) {
                this.inputList[index]["to_date"] = e.target.value
            }
            localStorage.setItem('timelineData', JSON.stringify(this.inputList))
            console.log(localStorage.getItem('timelineData'))

        },
        addInput(e) {
            e.preventDefault()
            this.inputList.push({
                from_date: "",
                to_date: "",
                episode: ""
            })
        },
        deleteInput(e, counter) {
            e.preventDefault()
            this.inputList.splice(counter, 1);
        },
        resetForm(e) {
            e.preventDefault()
            this.inputList = [
                {
                    from_date: "",
                    to_date: "",
                    episode: ""
                }
            ]
            document.querySelector("#tableContainer").innerHTML = ""
            document.querySelector("#chartContainer > iframe").src = ""
            localStorage.clear()
        }
    },
    computed: {
    },
    mounted() {
        if (localStorage.getItem('timelineData')) {
            this.inputList = JSON.parse(localStorage.getItem('timelineData'))
        }
    },
    provide() {
        return {
            addInput: this.addInput,
            deleteInput: this.deleteInput

        }
    }


}
</script>

<style >
.container {
    display: flex;
    justify-content: center;

}

.dataframe {
    max-width: 50%;
}
</style>