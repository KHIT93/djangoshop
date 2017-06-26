
window._ = require('lodash');
var Cookies = require('js-cookie');

import Vue from 'vue';
import axios from 'axios';


window.Vue = Vue;

/**
 * We'll load the axios HTTP library which allows us to easily issue requests
 * to our Laravel back-end. This library automatically handles sending the
 * CSRF token as a header based on the value of the "XSRF" token cookie.
 */

window.axios = axios;

window.axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken');
window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

window.axios.interceptors.request.use(request => {
  console.log('Starting Request', request)
  return request
})
