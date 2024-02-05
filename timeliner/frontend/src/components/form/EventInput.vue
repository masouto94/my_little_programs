<template>
    <div>
    Fecha<input type="text" label="date" name="date" :value="date">
    Episodio<input type="text" label="episode" name="episode" :value="episode" >
</div>
</template>

<script>
export default {
    name: 'EventInput',
    props:{
        index: Number
    },
    data() {
       return{

            date:"",
            episode:""

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