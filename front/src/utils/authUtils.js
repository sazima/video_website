function getUserInfo() {
    const token = localStorage.getItem("token")
    if (!token){
        return null;
    }
    const email = localStorage.getItem("email")
    return {
        token,
        email: email,
        nickName: localStorage.getItem("nickName") || email
    }
}
function setToken(userInfo) {
    localStorage.setItem('token', userInfo.token)
    localStorage.setItem('email', userInfo.email)
    localStorage.setItem('nickName', userInfo.nickName)
}

function cleanToken() {
    localStorage.removeItem('token')
    localStorage.removeItem('email')
    localStorage.removeItem('nickName')
}
export {getUserInfo, setToken, cleanToken}