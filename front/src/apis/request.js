import axios from 'axios'
// import {MessageBox, Message} from 'element-ui'
import store from '@/store'
import {aes_decrypt, toast} from "@/utils/utils";
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
        //

        let res = response.data
        if (response.headers['encrypt-key']) {
            const encrypt_text = res.slice(0, -32)
            const iv = res.slice(-32, -16)
            const key = res.slice(-16)
            const responseString = aes_decrypt(encrypt_text, key, iv)
            if (!responseString) {
                toast('系统错误')
                return Promise.reject(new Error('系统错误'))
            }
            res = JSON.parse(responseString)
        }

        // if the custom code is not 20000, it is judged as an error.
        if (res.code !== 200) {
            toast(res.msg)
            return Promise.reject(new Error(res.msg))
        } else {
            return res.data
        }
    },
    error => {
        toast('err' + error)
        return Promise.reject(error)
    }
)

export default request
