<template>
    <div>
    Fecha<input type="date" label="date" name="date" :value="date">
    Episodio<input type="text" label="episode" name="episode" :value="episode">
    <button @click="(e) => deleteInput(e,counter)">-</button>
    <button @click="addInput">+</button>
</div>
</template>

<script>
export default {
    name: 'EventInput',
    props:{
        date:String,
        episode:String
    },
    inject:[
        'addInput',
        'deleteInput'

    ],
    data() {
       return{

           

       }
    },
    methods: {
    },
    computed: {
    },
    mounted() {
  }
        

}
</script>

<style scoped>

</style>