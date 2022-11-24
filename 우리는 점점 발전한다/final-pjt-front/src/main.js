import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import VueDragscroll from "vue-dragscroll";


Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueDragscroll);


new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
