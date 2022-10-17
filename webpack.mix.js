const mix = require("laravel-mix");

mix
  .sass("assets/css/site.scss", "dist")
  .js("assets/js/site.js", "dist")
  .setPublicPath("assets")
  .browserSync({
    open: false,
    notify: false,
    proxy: "https://ffwenns.test",
    files: ["site/**/*.php", "assets/dist/*.{css,js}"],
    https: {
      cert: "localhost.pem",
      key: "localhost-key.pem",
    },
  });
