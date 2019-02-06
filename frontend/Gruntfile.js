const sass = require('node-sass');
module.exports = function(grunt) { // the general grunt function that is run

  grunt.initConfig({ // here we setup our config object with package.json and all the tasks

      pkg: grunt.file.readJSON('package.json'),

      sass: { // sass tasks
          dist: {
              options: {
                  implementation: sass,
                  'sourcemap=none': false
              },
              files: {
                  'style.css': 'scss/main.scss', // this is our main scss file
              }
          }
      }, 

      cssmin: { // minifying css task
          dist: {
              files: {
                  'style.min.css': 'style.css'
              }
          }
      },

      watch: { // watch task for general work
          sass: {
              files: ['scss/**/*.scss'],
              tasks: ['sass']
          },
          styles: {
              files: ['style.css'],
              tasks: [ 'cssmin']
          }
      },

      postcss: {
          options: {
              map: true, // inline sourcemaps

              processors: [
                  require('autoprefixer')({browsers: 'last 2 versions'})
              ]
          },
          dist: {
              src: 'style.css'
          }
      }
  });

  // all the plugins that is needed for above tasks
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-postcss');


  // registering the default task that we're going to use along with watch
  grunt.registerTask('default',['sass', 'cssmin', 'postcss:dist', 'watch']);
  grunt.registerTask('build',['sass', 'cssmin', 'postcss:dist']);
};

