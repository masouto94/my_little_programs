import { createApp } from 'vue'
import {router} from './router/routes.js'
import App from './App.vue'

createApp(App)
    .use(router)
.mount('#app')
