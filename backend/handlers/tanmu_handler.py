import datetime
import json
from collections import defaultdict
from typing import List

from tornado_request_mapping import request_mapping

from dao.tanmu_dao import TanmuDao
from dao.vod_dao import VodDao
from mixins.video_handler_mixin import VideoHandlerMixin
from models.tanmu import Tanmu
from utils.base_handler import BaseHandler
from utils.logger_factory import LoggerFactory
from utils.response import NotFoundResponse, Response, FuckYouResponse, ErrorResponse
from vo.video_detail_vo import Url


@request_mapping('/api/tanmu')
class TanmuHandler(BaseHandler, VideoHandlerMixin):
    logger = LoggerFactory.get_logger()

    @request_mapping('/get_by_video')
    async def get_by_video(self):
        vod_id = self.get_argument('vod_id')
        play_line_name = self.get_argument('play_line_name')
        play_name = self.get_argument('play_name')
        self.logger.info(f'获取弹幕 ip: {self.get_remote_ip()}, vod_id: {vod_id}, {play_line_name} - {play_name}')

        if not vod_id or not play_line_name or not play_name:
            return self.send_response(NotFoundResponse())
        tanmu_list = await TanmuDao.get_by_video_play_name(int(vod_id), play_line_name, play_name)
        return_dict = defaultdict(list)
        return_dict.update({1: [{'content': '发送一条弹幕试试吧'}, {'content': '弹幕有你更精彩'}]})
        for tanmu in tanmu_list:
            return_dict[tanmu['current_time_int']].append(tanmu)
        self.send_response(Response(return_dict))

    @request_mapping('/create', method='post')
    async def create(self):
        data = json.loads(self.request.body)
        vod_id = int(data.get('vod_id'))
        content = data.get('content')
        play_url = data.get('play_url')
        play_name = data.get('play_name')  # 比如bd高清
        play_line_name = data.get('play_line_name')  # 比如播放地址1
        current_time = float(data.get('current_time'))
        user_id = 1
        self.logger.info(f'发送弹幕 ip: {self.get_remote_ip()}, {vod_id} {play_line_name} - {play_name} content: {content}')
        if not content:
            return self.send_response(ErrorResponse('内容不能为空'))
        if current_time < 0:
            return self.send_response(FuckYouResponse())
        if not await self.check_play_url_and_play_name(play_url, play_name, play_line_name, int(vod_id)):
            return self.send_response(NotFoundResponse(msg='发送失败'))
        insert_data = {  # type: Tanmu
            'vod_id': vod_id,
            'content': content,
            'play_line_name': play_line_name,
            'play_url': play_url,
            'play_name': play_name,
            'current_time': current_time,
            'current_time_int': int(current_time),
            'styles': '',
            'user_id': user_id,
            'create_time': datetime.datetime.now()
        }
        return_id = await TanmuDao.insert_danmu(insert_data)
        self.logger.info(f'发送弹幕成功 ip: {self.get_remote_ip()}, id ->{return_id}, {insert_data}')
        self.send_response(Response({'id': 0}))

    # 验证该播放链接是否是该视频的
    async def check_play_url_and_play_name(self, play_url: str, play_name: str, play_line_name: str, vod_id: int, ) -> bool:
        if not play_url or '$' in play_url or not play_url.startswith('http') or not play_url.endswith('m3u8'):
            return False
            # return self.send_response(NotFoundResponse('链接错误'))
        if not play_name or '$' in play_name or 'http' in play_name:
            return False
        vod_video = await VodDao.get_by_vod_id(int(vod_id))
        if not vod_video:
            return False
        urls_list: List[Url] = self._parse_vod_play_url(vod_video['vod_play_url'])
        for url in urls_list:
            if url['play_line_name'] == play_line_name:
                for link_dict in url['links']:
                    if play_name == link_dict['name']:
                        if play_url == link_dict['link']:
                            return True
                        else:
                            return False
        return False
