const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const MiniCssExtractplugin = require('mini-css-extract-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const CompressionPlugin = require('compression-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    module: {
        rules: [{
                test: /\.(scss)$/,
                use: [{
                    loader: 'style-loader', // inject CSS to page
                }, {
                    loader: 'css-loader', // translates CSS into CommonJS modules
                }, {
                    loader: 'postcss-loader', // Run post css actions
                    options: {
                        plugins: function () { // post css plugins, can be exported to postcss.config.js
                            return [
                                require('precss'),
                                require('autoprefixer')
                            ];
                        }
                    }
                }, {
                    loader: 'sass-loader' // compiles Sass to CSS
                }]
            }, {
                test: /\.vue$/,
                loader: 'vue-loader'
            }, {
                test: /\.(png|jpe?g|gif)$/i,
                use: [
                    {
                        loader: 'file-loader',
                    },
                ],
            }, {
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader',
                ]
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin(),
        new MiniCssExtractplugin(),
        // new CleanWebpackPlugin(),
        new CompressionPlugin(),
        new CopyPlugin({
            patterns: [
                // { from: './src/resources/whiteboard/', to: './whiteboard' },
                { from: './src/resources/NearBeach.png', to: '' },
                { from: './src/resources/NearBeach_Small.png', to: '' },
                { from: './src/resources/images/', to: './images' },

                //TinyMce Files
                { from: './node_modules/tinymce/tinymce.min.js', to: './tinymce/tinymce.min.js' },
                { from: './node_modules/tinymce/skins/ui/oxide/skin.min.css', to: './tinymce/skins/ui/oxide/skin.min.css' },
                { from: './node_modules/tinymce/skins/content/default/content.min.css', to: './tinymce/skins/content/default/content.min.css' },
                { from: './node_modules/tinymce/skins/ui/oxide/content.min.css', to: './tinymce/skins/ui/oxide/content.min.css' },
                { from: './node_modules/tinymce/themes/silver/theme.min.js', to: './tinymce/themes/silver/theme.min.js' },
                { from: './node_modules/tinymce/icons/default/icons.min.js', to: './tinymce/icons/default/icons.min.js' },
            ],
        }),
        new HtmlWebpackPlugin({
            title: 'Production',
        }),
    ],
    entry: {
        'NearBeach': './src/js/app.js',
        'login': './src/js/login.js',
        // 'whiteboard': './src/js/whiteboard.js',
        'loader': './src/js/loader.js',
    },
    output: {
        path: path.resolve(__dirname, 'NearBeach/static/NearBeach'),
        filename: '[name].min.js'
    },
    // optimization: {
    //     runtimeChunk: 'single',
    // }
};