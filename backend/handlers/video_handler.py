import datetime
from typing import List

from tornado_request_mapping import request_mapping

from dao.type_dao import TypeDao
from dao.vod_dao import VodDao
from utils.base_handler import BaseHandler
from utils.entity_utils import EntityUtils
from utils.response import Response, NotFoundResponse
from vo.type_vo import TypeVo
from vo.video_detail_vo import Url, VideoDetailVo
from vo.video_list_vo import VodListVo


@request_mapping("/api/video")
class VideoHandler(BaseHandler):

    @request_mapping('/get_list', 'get')
    async def get_list(self):
        type_en = self.get_argument('type_en', '')
        page = int(self.get_argument('page') or 1)
        per_page = int(self.get_argument('per_page') or 36)
        kw = self.get_argument('kw', '')
        start = (page - 1) * per_page
        type_id = 0
        if type_en:
            type_by_en = await TypeDao.get_by_type_en(type_en)
            if not type_by_en:
                type_id = type_by_en['type_id']
        vod_list = await VodDao.get_by_query(type_id, kw, start, per_page)
        total = await VodDao.count_by_query(type_id, kw)
        return_list = list()  # type: List[VodListVo]
        for video in vod_list:
            vod_vo = EntityUtils.convert(video, VodListVo)
            vod_vo['vod_time'] = datetime.datetime.fromtimestamp(video['vod_time'])
            return_list.append(vod_vo)
        self.send_response(Response({
            'total': total,
            'data': return_list
        }))

    @request_mapping('/get_by_id', 'get')
    async def get_by_id(self):
        vod_id = self.get_argument('vod_id')
        if not vod_id:
            self.send_response(NotFoundResponse())
        vod = await VodDao.get_by_vod_id(int(vod_id))
        return_dict = {  # type: VideoDetailVo
            'vod_id': vod_id,
            'vod_name': vod['vod_name'],
            'urls': self._parse_vod_play_url(vod['vod_play_url'])
        }
        self.send_response(Response(return_dict))

    @request_mapping("/get_type_list", 'get')
    async def get_type_list(self):
        all_type = await TypeDao.get_all_type()
        self.send_response(Response(EntityUtils.list_convert(all_type, TypeVo)))

    @staticmethod
    def _parse_vod_play_url(play_url: str) -> List[Url]:
        if play_url.startswith('http'):
            return [{
                'play_line_name': '播放地址1',
                'links': [{'name': '在线播放', 'link': play_url}]
            }]
        play_group_links = play_url.split('$$$')
        play_group_links_list = []
        for index, links in enumerate(play_group_links):
            name_eps = links.split('$$')
            links = []
            for eps in name_eps:
                for ep in eps.split('#'):
                    name, link = ep.split('$')
                    links.append({
                        'name': name,
                        'link': link
                    })
            play_group_links_list.append({
                'play_line_name': '播放地址{}'.format(index + 1),
                'links': links
            })
        return play_group_links_list
