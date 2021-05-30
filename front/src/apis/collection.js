import request from "./request";
async function getAll() {
    const url = '/admin/collection/getAll'
    return request.get(url)
}
async function startCollection(key, hour) {
    const url = '/admin/collection/startTask'
    return request.get(url, {params: {key, hour}})
}
async function getTaskByKey(key) {
    const url = '/admin/collection/getTaskByKey'
    return request.get(url, {params: {key}})
}
export {getAll, startCollection, getTaskByKey}
