const UglifyPlugin = require('uglifyjs-webpack-plugin')

// vue.config.js
module.exports = {

  configureWebpack: config => {
    console.log(config);
    if (process.env.NODE_ENV === 'production') {
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
    } else {
      // 为开发环境修改配置...
    }
  }
}
