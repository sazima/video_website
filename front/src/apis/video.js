import request from "./request";

async function getVideoList(params) {
  const url = '/video/get_list'
  return request.get(url, {params})
}

async function getVideoById(vod_id) {
  const url = '/video/get_by_id'
  return request.get(url, {params: {vod_id: vod_id}})

}

export {getVideoList, getVideoById}
