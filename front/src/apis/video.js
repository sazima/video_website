import request from "./request";

async function getVideoList(params) {
    const url = '/video/get_list'
    return request.get(url, {params})
}

async function getVideoById(vod_id) {
    const url = '/video/get_by_id'
    return request.get(url, {params: {vod_id: vod_id}})

}

async function getTypes() {
    const url = '/video/get_type_list'
    return request.get(url)
}

async function addTanmu(data) {
    const url = '/tanmu/create'
    return request.post(url, data)
}

async function getTanmu(params) {
    const url = '/tanmu/get_by_video'
    return request.get(url, {params})
}
export {getVideoList, getVideoById, getTypes, addTanmu, getTanmu}
