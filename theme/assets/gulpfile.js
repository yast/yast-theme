const gulp = require('gulp'),
  sass = require('gulp-sass')(require('sass')),
  rename = require('gulp-rename');

// Folders to take the assets from & place the generated files
const destination = '../SLE/'
const origin = 'scss/*scss'


let path = {
  src_sass:'scss/*scss',
  src_destination:'../SLE/wizard/',
}

gulp.task("sassTask", function() {
  return gulp
    .src(path.src_sass)
    .pipe(sass().on('error', sass.logError))
    .pipe(rename({ extname: '.qss' }))
    .pipe(gulp.dest(path.src_destination))
});


// gulp default (sass, minify-css, browser-sync) methodqt for
// gulp.task('default', 'sassTask')
gulp.task('default', gulp.series('sassTask'));
