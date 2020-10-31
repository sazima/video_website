import datetime
from typing import List

from tornado_request_mapping import request_mapping

from dao.type_dao import TypeDao
from dao.vod_dao import VodDao
from models.mac_vod import MacVod
from utils.base_handler import BaseHandler
from utils.entity_utils import EntityUtils
from utils.redis_cache import RedisCache
from utils.response import Response
from vo.type_vo import TypeVo


@request_mapping('/api/index')
class IndexHandler(BaseHandler):

    @request_mapping("/indexTree", 'get')
    async def get_index_tree(self):
        key = 'index_tree'
        response_cache = RedisCache.get(key)
        if response_cache:
            return self.send_response(response_cache)
        type_with_video_list = list()
        all_types = await TypeDao.get_all_type()
        brand_video = await VodDao.get_brand_video()
        all_types_vo = list()
        for type_ in all_types:
            all_types_vo.append(EntityUtils.convert(type_, TypeVo))
            if type_['type_pid'] == 0:
                video_by_type = await VodDao.get_index_video_by_type_id(type_['type_id'], 18)
                type_with_video_list.append({
                    'type_id': type_.get('type_id'),
                    'type_name': type_.get('type_name'),
                    'type_en': type_.get('type_en'),
                    'type_sort': type_.get('type_sort'),
                    'videos': self._video_model_to_vo(video_by_type)
                })
        response = Response({
            'brand': self._video_model_to_vo(brand_video),
            'all_types': all_types_vo,
            'type_with_video_list': type_with_video_list
        })
        RedisCache.set(key, response)
        self.send_response(response)

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
