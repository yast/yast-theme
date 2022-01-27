const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const rename = require('gulp-rename');

let path = {
  src_sass: 'scss/installation.scss',
  src_sass_light: 'scss/installation-light.scss',
  src_destination: '../SLE/wizard/',
}

gulp.task("theme-dark", function() {
  return gulp
    .src(path.src_sass)
    .pipe(sass().on('error', sass.logError))
    .pipe(rename({ extname: '.qss' }))
    .pipe(gulp.dest(path.src_destination))
});

gulp.task("theme-light", function() {
  return gulp
    .src(path.src_sass_light)
    .pipe(sass().on('error', sass.logError))
    .pipe(rename({ extname: '.qss' }))
    .pipe(gulp.dest(path.src_destination))
});

gulp.task('default', gulp.series('theme-dark', 'theme-light'));
