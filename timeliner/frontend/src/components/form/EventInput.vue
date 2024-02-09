<template>
    <div>
    Fecha inicio<input type="date" label="from_date" name="from_date" :value="from_date">
    Fecha fin<input type="date" label="to_date" name="to_date" :value="to_date">
    Episodio<input type="text" label="episode" name="episode" :value="episode">
    <button @click="(e) => deleteInput(e,counter)">-</button>
    <button @click="addInput">+</button>
</div>
</template>

<script>
export default {
    name: 'EventInput',
    props:{
        from_date:String,
        to_date:String,
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