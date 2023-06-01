import { createApp } from 'vue'
import { createI18n } from 'vue-i18n/index.mjs'
import { content } from './locales/content'
import FlagIcon from 'vue-flag-icon'

import App from './App.vue'

const i18n = createI18n({
    locale: 'es',
    fallbackLocale: 'en',
    messages:content
})
const app = createApp(App)
app.use(i18n)
app.use(FlagIcon)
app.mount('#app')
