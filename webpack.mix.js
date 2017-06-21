const { mix } = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */

mix.js('assets/src/js/frontend.js', 'assets/dist/js')
   .js('assets/src/js/backend.js', 'assets/dist/js')
   .sass('assets/src/sass/app.scss', 'assets/dist/css')
   .stylus('assets/src/stylus/backend.styl', 'assets/dist/css');
