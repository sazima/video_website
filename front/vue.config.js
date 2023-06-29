const UglifyPlugin = require('uglifyjs-webpack-plugin')


module.exports = {

  configureWebpack: config => {
    const env = process.env.NODE_ENV
    if (env === 'production') {
      // 为生产环境修改配置...
      let optimization = {
        minimizer: [new UglifyPlugin({
          uglifyOptions: {
            warnings: false,
            compress: {
              drop_console: true,
              drop_debugger: false,
              pure_funcs: ['console.log']
            }
          }
        })]
      }
      Object.assign(config, {
        optimization
      })
    } else if (env === 'development'){
      // 为开发环境修改配置...
    } else {
        //
    }
  },
  outputDir: process.env.NODE_ENV === 'production' ? 'dist' : 'video_cordova/www',
  publicPath: '/'
}
