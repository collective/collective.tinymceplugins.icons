const path = require("path");
const mfc = require("@patternslib/dev/webpack/mf_config");

module.exports = (env, argv) => {
  let config = {
    entry: {
      "plugin": "./src/collective/tinymceplugins/icons/browser/static/plugin.js",
    },
    output: {
      path: path.resolve(__dirname, "src/collective/tinymceplugins/icons/browser/static"),
      filename: "[name].js",
    },
  };

  if (argv.mode === "production") {
    config.output.filename = "[name].min.js";
  }

  return config;
};
