import VueRouter from 'vue-router'
import login from "@/components/login";
import registration from "@/components/registration";
import home from "@/components/home";
import authorization from "@/components/authorization";

export default new VueRouter({
        routes: [
            {
                path: '',
                component: authorization,
                // beforeEnter: (to, from, next) => {
                //
                // }
            },
            {
                path: '/home',
                name: 'home',
                component: home
            },
            {
                path: '/signup',
                name: 'reg',
                component: registration
            },
            {
                path: '/login',
                name: 'login',
                component: login
            }
        ],
        //отключение хеша '#'
        mode: 'history'
    }
)