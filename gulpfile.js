const { src, dest, watch, series } = require("gulp");
var sass = require("gulp-sass")(require("sass"));
const prefix = require("gulp-autoprefixer");
const minfy = require("gulp-clean-css");
const rename = require("gulp-rename");

// function
function compilesass() {
  return src("./app/scss/main.scss")
    .pipe(sass())
    .pipe(prefix())
    .pipe(minfy())
    .pipe(
      rename(function (path) {
        return {
          dirname: path.dirname + "",
          basename: path.basename + ".min",
          extname: ".css",
        };
      })
    )
    .pipe(dest("./app/css"));
}

// watchtask
function watchTask() {
  watch("./app/scss/**/*.scss", compilesass);
}

// default gulp
exports.default = series(compilesass, watchTask);
