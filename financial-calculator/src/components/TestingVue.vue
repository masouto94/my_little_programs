<template>
    <div>
        <h1>HOLA</h1>
        <h2>{{date}}</h2>
    </div>
</template>
<script>
export default {
    name: 'TestingVue',
    props:{
        date: Date
    }
}
</script>
<style scoped>
h1{
    color: blue;
}
h2{
    color:red;
}
</style>