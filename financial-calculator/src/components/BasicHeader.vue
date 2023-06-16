<template>
    <div>
            <nav id="navBar">
                    <span class="langFlag"><flag @click="setLocale"  iso="ar" lang="es"/></span>
                    <span class="langFlag"><flag @click="setLocale" iso="us" lang="en"/></span>
            </nav>

        <div>
        <a href="https://www.vecteezy.com/free-vector/graph" target="_blank">
            <img id="financialChart"  src="../assets/financeChart.jpg" alt="Graph Vectors by Vecteezy" srcset="">
        </a>
        <h1> {{ $t("header.title") }} </h1>
    </div>
    </div> 
</template>

<script>
export default {
    name: 'BasicHeader',
    data() {
        return {
        }
    },
    methods: {
        setLocale: function(e){
            const lang = e.target.getAttribute('lang')
            this.$i18n.locale = lang
        }
    },
    computed: {
    },
    mounted() {
  }
        

}
</script>

<style scoped>
#financialChart{
    width: 200px;
    height: 200px;

}

#navBar{
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: baseline;
}

.langFlag{
    font-size: 50px;
}

</style>

