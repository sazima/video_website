from tornado_request_mapping import request_mapping

from dao.type_dao import TypeDao
from dao.vod_dao import VodDao
from utils.base_handler import BaseHandler
from utils.response import Response


@request_mapping('/api/index')
class IndexHandler(BaseHandler):

    @request_mapping("/indexTree", 'get')
    async def get_index_tree(self):
        return_list = list()
        parent_types = await TypeDao.get_type_by_pid(0)
        for type_ in parent_types:
            vod_list = await VodDao.get_index_vod_by_type_id(type_['type_id'], 6)
            return_list.append({
                'type_id': type_.get('type_id'),
                'type_name': type_.get('type_name'),
                'type_en': type_.get('type_en'),
                'type_sort': type_.get('type_sort'),
                'videos': vod_list
            })
        self.send_response(Response(return_list))
