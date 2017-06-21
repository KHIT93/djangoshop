
/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries. It is a great starting point when
 * building robust, powerful web applications using Vue and Laravel.
 */

import './bootstrap';

import Vuetify from 'vuetify';
import VueRouter from 'vue-router';
import NotFound from './components/NotFound.vue';


Vue.use(Vuetify);
Vue.use(VueRouter);

const routes = [

    /** Catchall route to display 404 page */
    { path: '*', component: NotFound }
];

const router = new VueRouter({
    routes
});

/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */

const app = new Vue({
    el: '#app',
    router,
    data:
    {
    },
    methods:
    {
    }
});

