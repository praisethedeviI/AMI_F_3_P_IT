import Vue from 'vue'
import Vuex from 'vuex'
import {Note} from '@/api/notes'
import {User} from '@/api/users'
import {ADD_NOTE, ADD_USER, REMOVE_NOTE, REMOVE_USER, SET_NOTES, SET_USERS} from './mutation-types.js'


Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        notes: [],
        users: []
    },
    getters: {
        notes: state => state.notes,
        users: state => state.users
    },
    mutations: {
        [ADD_NOTE](state, note) {
            state.notes = [note, ...state.notes]
        },
        [REMOVE_NOTE](state, {id}) {
            state.notes = state.notes.filter(note => {
                return note.id !== id
            })
        },
        [SET_NOTES](state, {notes}) {
            state.notes = notes
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
