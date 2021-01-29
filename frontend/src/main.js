import Vue from 'vue'
import App from './App'
import store from './store'
import Vuex from "vuex"
import Vuelidate from 'vuelidate'
import {BootstrapVue} from 'bootstrap-vue'

Vue.config.productionTip = false
Vue.use(Vuelidate)
Vue.use(BootstrapVue)
Vue.use(Vuex)

new Vue({
    render: h => h(App),
    store
}).$mount('#app')