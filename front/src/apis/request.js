import axios from 'axios'
// import {MessageBox, Message} from 'element-ui'
import store from '@/store'
// import {getToken} from '@/utils/auth'

// create an axios instance
const request = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL, // url = base url + request url
  timeout: 10000 // request timeout
})

request.interceptors.request.use(
  config => {

    if (store.getters.token) {
      // config.headers['X-Token'] = getToken()
    }
    return config
  },
  error => {
    // do something with request error
    console.log(error) // for debug
    return Promise.reject(error)
  }
)

// response interceptor
request.interceptors.response.use(
  response => {
    const res = response.data

    // if the custom code is not 20000, it is judged as an error.
    if (res.code !== 200) {
      return Promise.reject(new Error(res.message || 'Error'))
    } else {
      return res.data
    }
  },
  error => {
    alert('err' + error)
    return Promise.reject(error)
  }
)

export default request
