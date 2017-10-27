var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var concat = require('gulp-concat');
var livereload = require('gulp-livereload');

var bootstrapDir = './node_modules/bootstrap-sass/assets';
var flickityDir = './node_modules/flickity/dist';
var jqueryDir = './node_modules/jquery/dist';
var waypointsDir = './node_modules/waypoints/lib';

gulp.task('sass', function() {
  return gulp.src('css/style.scss')
            .pipe(sass({
              includePaths: [
                bootstrapDir + '/stylesheets',
                flickityDir
              ]
            }).on('error', sass.logError))
            .pipe(gulp.dest('./css/'))
            .pipe(livereload());
});

gulp.task('templates', function() {
  livereload.reload();
});

var bootstrapJsDir = bootstrapDir + '/javascripts/bootstrap';
var jsFiles = [

  jqueryDir + '/jquery.slim.min.js',
  flickityDir + '/flickity.pkgd.min.js',
  waypointsDir + '/jquery.waypoints.min.js',
  './js/navigation.js',
  './js/callout-fullwidth.js'
];
gulp.task('js', function() {
  return gulp.src(jsFiles)
          .pipe(concat('scripts-all.js'))
          .pipe(gulp.dest('./js/'))
          .pipe(livereload());
});

gulp.task('watch', function() {
  livereload.listen();
  gulp.watch('css/**/*.scss', ['sass']);
  gulp.watch('../../**/*.html', ['templates']);
  gulp.watch(jsFiles, ['js']);
});

gulp.task('default', ['watch']);
