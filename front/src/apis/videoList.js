import request from "./request";

async function getVideoList(params) {
  const url = '/video/get_list'
  return request.get(url, {params})
}
export {getVideoList}
