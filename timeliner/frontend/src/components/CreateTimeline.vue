<template>
  <div class="timeline">
    <h1>{{ timelineData }}</h1>
    <form  action="/dataentry" @submit="sendData" method="post">
      Name<input type="text" label="name" name="name" v-model="dataentry.name">
      Department<input type="text" label="department" name="department" v-model="dataentry.department">
      <input type="submit" value="SEND">
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'CreateTimeline',
  props: {
    timelineData: String
  },
    data() {
        return {
            dataentry: {
                name: "",
                department: ""
            }
        };
    },
    methods: {
        sendData: function (e) {
          e.preventDefault()
            const path = `http://127.0.0.1:5000/dataentry`
            console.log(path)
            axios.post(path, {
                name: this.dataentry.name,
                department: this.dataentry.department,
            }
            )
                .then(response => {
                    console.log(response);
                })
                .catch(err => { console.log(err);
                });
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
