import Vue from 'vue'
import App from './App.vue'
import Vuex from "vuex"
import Vuelidate from 'vuelidate'
import {BootstrapVue} from 'bootstrap-vue'

Vue.config.productionTip = false
Vue.use(Vuelidate)
Vue.use(BootstrapVue)
Vue.use(Vuex)

new Vue({
    render: h => h(App),
}).$mount('#app')
