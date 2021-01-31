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
                //     // здесь проверьте залогинен ли пользователь, если нет, то редиректите его на страницу логина
                //     if (to.name !== 'Login' && !isAuthenticated ) next({name: login})
                //     else next()
                // },
                // meta: {requiresAuth: true}
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