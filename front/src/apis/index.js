import request from "./request";
async function getIndexTree() {
  const url = '/index/indexTree'
  return request.get(url)
}
export {getIndexTree}
