var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var concat = require('gulp-concat');
var livereload = require('gulp-livereload');
var strip = require('gulp-strip-comments');

var bootstrapDir = './node_modules/bootstrap-sass/assets';
var bootstrapJsDir = bootstrapDir + '/javascripts/bootstrap';
var owlDir = './node_modules/owl.carousel/dist';
var jqueryDir = './node_modules/jquery/dist';
var waypointsDir = './node_modules/waypoints/lib';
var touchSwipeDir = './node_modules/jquery-touchswipe';


gulp.task('sass', function() {
  return gulp.src('css/style.scss')
            .pipe(sass({
              includePaths: [
                bootstrapDir + '/stylesheets',
                owlDir + '/assets'
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
  jqueryDir + '/jquery.min.js',
  owlDir + '/owl.carousel.min.js',
  waypointsDir + '/jquery.waypoints.min.js',
  touchSwipeDir + '/jquery.touchSwipe.min.js',
  bootstrapJsDir + '/modal.js',
  './js/utils.js',
  './js/image-lazy-load.js',
  './js/navigation.js',
  './js/callout-fullwidth.js',
  './js/slider.js',
  './js/image-overlay.js',
  './js/video-overlay.js',  
  './js/rings.js',
  './js/page-transitions.js',
  './js/innovation-carousel.js'
];
gulp.task('js', function() {
  return gulp.src(jsFiles)
          .pipe(strip())
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
