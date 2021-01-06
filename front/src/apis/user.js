import request from "./request";
async function login(data) {
    const url = '/user/login'
    return request.post(url, data)
}
async function registerUser(data) {
    const url = '/user/register'
    return request.post(url, data)
}
async function getLoginStatus() {
    const url = '/user/loginStatus'
    return request.get(url)

}
export {login, registerUser, getLoginStatus}

