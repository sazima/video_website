import Vue from 'vue'
import layout from "./components/layout";
import router from './router'
import store from './store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/global.css'
import "video.js/dist/video-js.min.css"
import "@silvermine/videojs-quality-selector/dist/css/quality-selector.css"
import VConsole from 'vconsole'

// if (process.env.NODE_ENV === 'development') {
new VConsole()
// }
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.productionTip = false

const vue = new Vue({
  router,
  store,
  render: h => h(layout)
}).$mount('#app')


export default vue