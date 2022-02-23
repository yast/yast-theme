const gulp = require('gulp');
const gulpStylelint = require('gulp-stylelint');
const sass = require('gulp-sass')(require('sass'));
const rename = require('gulp-rename');

let path = {
  src_sass: 'scss/installation.scss',
  src_sass_light: 'scss/installation-light.scss',
  src_sass_wb: 'scss/white-black.scss',
  src_sass_cb: 'scss/cyan-black.scss',
  src_sass_highcontrast: 'scss/highcontrast.scss',
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

gulp.task('theme-white-black', function() {
  return gulp
    .src(path.src_sass_wb)
    .pipe(sass().on('error', sass.logError))
    .pipe(rename({ extname: '.qss' }))
    .pipe(gulp.dest(path.src_destination))
});

gulp.task('theme-cyan-black', function() {
  return gulp
    .src(path.src_sass_cb)
    .pipe(sass().on('error', sass.logError))
    .pipe(rename({ extname: '.qss' }))
    .pipe(gulp.dest(path.src_destination))
});

gulp.task('theme-highcontrast', function() {
  return gulp
    .src(path.src_sass_highcontrast)
    .pipe(sass().on('error', sass.logError))
    .pipe(rename({ extname: '.qss' }))
    .pipe(gulp.dest(path.src_destination))
});

gulp.task('lint-css', function () {
  return gulp
    .src('../SLE/wizard/installation*.qss')
    .pipe(gulpStylelint({
      reporters: [
        {formatter: 'string', console: true}
      ]
    }));
});

gulp.task('lint-scss', function () {
  return gulp
    .src('**/*.scss')
    .pipe(gulpStylelint({
      reporters: [
        {formatter: 'string', console: true}
      ]
    }));
});

gulp.task('lint', gulp.series('lint-scss', 'lint-css'));

gulp.task('default', gulp.series(
  'theme-cyan-black',
  'theme-dark',
  'theme-highcontrast',
  'theme-light',
  'theme-white-black'
));
