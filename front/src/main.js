import Vue from 'vue'
import App from "./components/App";
import userLayout from "./components/layout";
import adminLayout from "./components/adminLayout/DashboardLayout";
import router from './router'
import store from './store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/global.css'
import "video.js/dist/video-js.min.css"
import "@silvermine/videojs-quality-selector/dist/css/quality-selector.css"
import SidebarPlugin from './components/SidebarPlugin'
import NotificationsPlugin from './components/NotificationPlugin'
import VConsole from 'vconsole'


// if (process.env.NODE_ENV === 'development') {
new VConsole()
// }
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.component('userLayout', userLayout)
Vue.component('adminLayout', adminLayout)

Vue.config.productionTip = false
SidebarPlugin.install(Vue)
NotificationsPlugin.install(Vue)
Vue.directive('click-outside', {
  bind: function (el, binding, vnode) {
    el.clickOutsideEvent = function (event) {
      // here I check that click was outside the el and his children
      if (!(el == event.target || el.contains(event.target))) {
        // and if it did, call method provided in attribute value
        vnode.context[binding.expression](event);
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent)
  },
  unbind: function (el) {
    document.body.removeEventListener('click', el.clickOutsideEvent)
  },
});
const vue = new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')


export default vue