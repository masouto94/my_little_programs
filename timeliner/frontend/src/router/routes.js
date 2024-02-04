import { createRouter, createWebHistory } from 'vue-router'
import CreateTimeline from '../components/CreateTimeline.vue';
import HelloWorld from '../components/HelloWorld.vue'
export const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'CreateTimeline',
            component: CreateTimeline
        },
        {
            path: '/dummy',
            name: 'HelloWorld',
            component: HelloWorld
        }
    ]
})
