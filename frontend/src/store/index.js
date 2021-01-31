import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import {Note} from '@/api/notes'
import {User} from '@/api/users'
import {ADD_NOTE, ADD_USER, REMOVE_NOTE, REMOVE_USER, SET_NOTES, SET_USERS} from './mutation-types.js'

// Make Axios play nice with Django CSRF
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        all_notes: [],
        users: [],
        authUser: {},
        isAuthenticated: false,
        jwt: localStorage.getItem('token'),
        endpoints: {
            // TODO: Remove hardcoding of dev endpoints
            obtainJWT: 'http://localhost:8000/api/v1/auth/obtain_token/',
            refreshJWT: 'http://localhost:8000/api/v1/auth/refresh_token/',
            baseUrl: 'http://localhost:8000/api/v1'
        }
    },
    getters: {
        notes: state => state.all_notes,
        users: state => state.users
    },
    mutations: {
        setAuthUser(state, {authUser, isAuthenticated}) {
            Vue.set(state, 'authUser', authUser)
            Vue.set(state, 'isAuthenticated', isAuthenticated)
        },
        updateToken(state, newToken) {
            // TODO: For security purposes, take localStorage out of the project.
            localStorage.setItem('token', newToken);
            state.jwt = newToken;
        },
        removeToken(state) {
            // TODO: For security purposes, take localStorage out of the project.
            localStorage.removeItem('token');
            state.jwt = null;
        },

        [ADD_NOTE](state, note) {
            state.all_notes = [note, ...state.all_notes]
        },
        [REMOVE_NOTE](state, {id}) {
            state.all_notes = state.all_notes.filter(note => {
                return note.id !== id
            })
        },
        [SET_NOTES](state, {notes}) {
            state.all_notes = notes
        },

        [ADD_USER](state, user) {
            state.users = [user, ...state.users]
        },
        [REMOVE_USER](state, {id}) {
            state.users = state.users.filter(user => {
                return user.id !== id
            })
        },
        [SET_USERS](state, {users}) {
            state.users = users
        }
    },
    actions: {
        createNote({commit}, noteData) {
            Note.create(noteData).then(note => {
                commit(ADD_NOTE, note)
            })
        },
        deleteNote({commit}, noteData) {
            Note.delete(noteData).then(note => {
                commit(REMOVE_NOTE, note)
            })
        },
        getNotes({commit}) {
            Note.list().then(notes => {
                commit(SET_NOTES, {notes})
            })
        },

        createUser({commit}, userData) {
            User.create(userData).then(user => {
                commit(ADD_USER, user)
            })
        },
        deleteUser({commit}, userData) {
            User.delete(userData).then(user => {
                commit(REMOVE_USER, user)
            })
        },
        getUsers({commit}) {
            User.list().then(users => {
                commit(SET_USERS, {users})
            })
        }
    }
})
