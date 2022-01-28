const gulp = require('gulp');
const gulpStylelint = require('gulp-stylelint');
const sass = require('gulp-sass')(require('sass'));
const rename = require('gulp-rename');

let path = {
  src_sass: 'scss/installation.scss',
  src_sass_light: 'scss/installation-light.scss',
  src_destination: '../SLE/wizard/',
}

gulp.task('theme-dark', function() {
  return gulp
    .src(path.src_sass)
    .pipe(sass().on('error', sass.logError))
    .pipe(rename({ extname: '.qss' }))
    .pipe(gulp.dest(path.src_destination))
});

gulp.task('theme-light', function() {
  return gulp
    .src(path.src_sass_light)
    .pipe(sass().on('error', sass.logError))
    .pipe(rename({ extname: '.qss' }))
    .pipe(gulp.dest(path.src_destination))
});

gulp.task('lint-dark-css', function () {
  return gulp
    .src('../SLE/wizard/installation.qss')
    .pipe(gulpStylelint({
      reporters: [
        {formatter: 'string', console: true}
      ]
    }));
});

gulp.task('lint-light-css', function () {
  return gulp
    .src('../SLE/wizard/installation-light.qss')
    .pipe(gulpStylelint({
      reporters: [
        {formatter: 'string', console: true}
      ]
    }));
});

gulp.task('lint-css', gulp.series('lint-dark-css', 'lint-light-css'));

gulp.task('default', gulp.series('theme-dark', 'theme-light'));
