import VueRouter from 'vue-router'
import login from "@/components/login";
import registration from "@/components/registration";
import home from "@/components/home";
import authorization from "@/components/authorization";

export default new VueRouter({
        routes: [
            {
                path: '',
                component: authorization
            },
            {
                path: '/home',
                component: home
            },
            {
                path: '/signup',
                component: registration
            },
            {
                path: '/login',
                component: login
            }
        ],
        //отключение хеша '#'
        mode: 'history'
    }
)