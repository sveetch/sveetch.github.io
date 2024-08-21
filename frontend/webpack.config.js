const Path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    // Disable production-specific optimizations by default
    // They can be re-enabled by running the cli with `--mode=production` or making a
    // separate webpack config for production.
    mode: "development",

    // Every source path are resolved from current directory
    context: __dirname,

    // Entrypoint sources to build, every Javascript or Sass entrypoints have to be
    // defined as its own entry
    entry: {
        main: "./js/main.js",
    },

    // Built JS files goes into project staticfile directory
    output: {
        path: Path.resolve("../project/sources/js"),
        // filename: "js/[name].[contenthash:6].js",
        filename: "[name].js",
        publicPath: "/static/js/",
        // Ensure previous bundle builds are cleaned and do not stack forever
        clean: true,
    },

    // Modules rules
    module: {
        rules: [
            // Babel ES6 inspection watch for every JS sources changes
            {
                test: /\.js$/,
                include: Path.resolve(__dirname, 'js'),
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ["@babel/preset-env"]
                    },
                }
            },
        ]
    },

    // Enabled webpack plugins with their config
    plugins: [
        // Create/update manifest of built entries
        new BundleTracker({
            path: Path.join(__dirname, '../project/sources'),
            filename: 'js-assets.json'
        })
    ],
};
