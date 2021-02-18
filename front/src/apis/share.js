import request from "./request";
async function getUid() {
    const url = '/share/generateUid'
    return request.get(url)

}
export {getUid}
