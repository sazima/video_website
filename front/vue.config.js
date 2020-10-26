// vue.config.js
module.exports = {
  configureWebpack: config => {
    console.log(config);
    if (process.env.NODE_ENV === 'production') {
      // 为生产环境修改配置...
    } else {
      // 为开发环境修改配置...
    }
  }
}
