import request from "./request";

async function getVideoList(params) {
    const url = '/video/pageByQuery'
    return request.get(url, {params})
}

async function getVideoById(av) {
    const url = '/video/detail'
    return request.get(url, {params: {av: av}})

}

async function getTypes() {
    const url = '/type/getAll'
    return request.get(url)
}

async function addTanmu(data) {
    const url = '/tanmu/create'
    return request.post(url, data)
}

async function getTanmu(params) {
    const url = '/tanmu/getByVideo'
    return request.get(url, {params})
}
export {getVideoList, getVideoById, getTypes, addTanmu, getTanmu}
