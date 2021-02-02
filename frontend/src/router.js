import VueRouter from 'vue-router'
import login from "@/components/login";
import registration from "@/components/registration";
import home from "@/components/home";
import authorization from "@/components/authorization";
import axios from "axios";

const a = localStorage.getItem('token');
export default new VueRouter({
        routes: [
            {
                path: '',
                name: 'main',
                component: authorization,
                beforeEnter: (to, from, next) => {
                    axios.post('http://localhost:8000/api/v1/auth/verify_token/', {token: a}).then(() => {
                        window.location.href = "/home"
                    }).catch(error => {
                        console.log(error)
                        next()
                    })
                }
            },
            {
                path: '/home',
                name: 'home',
                component: home,
                beforeEnter: (to, from, next) => {
                    // check for valid auth token
                    axios.post('http://localhost:8000/api/v1/auth/verify_token/', {token: a}).then(() => {
                        next();
                    }).catch(error => {
                        console.log(error)
                        window.location.href = "/login";
                    })
                }
            },
            {
                path: '/signup',
                name: 'reg',
                component: registration
            },
            {
                path: '/login',
                name: 'login',
                component: login,
                beforeEnter: (to, from, next) => {
                    axios.post('http://localhost:8000/api/v1/auth/verify_token/', {token: a}).then(() => {
                        window.location.href = "/home"
                    }).catch(error => {
                        console.log(error)
                        next();
                    })
                }
            }
        ],
        //отключение хеша '#'
        mode: 'history'
    }
)