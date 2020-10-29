import datetime
from typing import List

from tornado_request_mapping import request_mapping

from dao.type_dao import TypeDao
from dao.vod_dao import VodDao
from models.mac_vod import MacVod
from utils.base_handler import BaseHandler
from utils.response import Response


@request_mapping('/api/index')
class IndexHandler(BaseHandler):

    @request_mapping("/indexTree", 'get')
    async def get_index_tree(self):
        type_with_video_list = list()
        parent_types = await TypeDao.get_type_by_pid(0)
        brand_video = await VodDao.get_brand_video()
        for type_ in parent_types:
            video_by_type = await VodDao.get_index_video_by_type_id(type_['type_id'], 18)
            type_with_video_list.append({
                'type_id': type_.get('type_id'),
                'type_name': type_.get('type_name'),
                'type_en': type_.get('type_en'),
                'type_sort': type_.get('type_sort'),
                'videos': self._video_model_to_vo(video_by_type)
            })
        self.send_response(Response({
            'brand': self._video_model_to_vo(brand_video),
            'type_with_video_list': type_with_video_list
        }))

    def _video_model_to_vo(self, video_list: List[MacVod]):
        vo_list = list()
        for vod in video_list:
            vo_list.append({
                'vod_id': vod['vod_id'],
                'vod_name': vod['vod_name'],
                'vod_time': datetime.datetime.fromtimestamp(vod['vod_time']),
                'vod_pic': vod['vod_pic']
            })
        return vo_list
