const gulp = require('gulp');
const gulpStylelint = require('gulp-stylelint');
const sass = require('gulp-sass')(require('sass'));
const rename = require('gulp-rename');
const header = require('gulp-header');

let path = {
  src_source: 'scss',
  src_destination: '../SLE/wizard/',
}

const themes = [
  'installation',
  'installation-light',
  'white-black',
  'cyan-black',
  'highcontrast'
];

const buildThemes = (done) => {
  const tasks = themes.flatMap((theme) => {
    function buildQSS() {
      return gulp
        .src(`${path.src_source}/${theme}.scss`)
        .pipe(sass().on('error', sass.logError))
        .pipe(rename({ extname: '.qss' }))
        .pipe(gulp.dest(path.src_destination))
    }

    function buildRichtextCSS() {
      let yastTheme = theme;

      if(theme === 'installation') yastTheme = 'dark';
      if(theme === 'installation-light') yastTheme = 'light';

      return gulp
        .src(`${path.src_source}/richtext.scss`)
        // Sass imports can't use interpolation, see https://sass-lang.com/documentation/at-rules/import#interpolation
        .pipe(header(`@import 'theme-vars/${yastTheme}';\n`))
        .pipe(sass().on('error', sass.logError))
        .pipe(rename({ basename: `${theme}_richtext`, extname: '.css' }))
        .pipe(gulp.dest(path.src_destination))
    }

    buildQSS.displayName = `buildQSS for '${theme}' theme`
    buildRichtextCSS.displayName = `buildRichtextCSS for '${theme}' theme`

    return [buildQSS, buildRichtextCSS];
  });

  return gulp.series(...tasks, (seriesDone) => {
    seriesDone();
    done();
  })();
};

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

gulp.task('default', gulp.series(buildThemes));
