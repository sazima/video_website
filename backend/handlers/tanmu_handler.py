import datetime
import json
from collections import defaultdict

from tornado_request_mapping import request_mapping

from dao.tanmu_dao import TanmuDao
from dao.vod_dao import VodDao
from utils.base_handler import BaseHandler
from utils.response import NotFoundResponse, Response, FuckYouResponse, ErrorResponse


@request_mapping('/api/tanmu')
class TanmuHandler(BaseHandler):

    @request_mapping('/get_by_video')
    async def get_by_video(self):
        vod_id = self.get_argument('vod_id')
        play_url = self.get_argument('play_url')
        if not vod_id or not play_url:
            return self.send_response(NotFoundResponse())
        tanmu_list = await TanmuDao.get_by_vod_id_and_play_url(int(vod_id), play_url)
        return_dict = defaultdict(list)
        return_dict.update({1: [{'content': '发送一条弹幕试试吧'}, {'content': '弹幕有你更精彩'}]} )
        for tanmu in tanmu_list:
            return_dict[tanmu['current_time_int']].append(tanmu)
        self.send_response(Response(return_dict))

    @request_mapping('/create', method='post')
    async def create(self):
        data = json.loads(self.request.body)
        vod_id = int(data.get('vod_id'))
        content = data.get('content')
        play_url = data.get('play_url')
        if not content:
            return self.send_response(ErrorResponse('内容不能为空'))
        current_time = float(data.get('current_time'))
        if current_time < 0:
            return self.send_response(FuckYouResponse())
        if not play_url or '$' in play_url or not play_url.startswith('http') or not play_url.endswith('m3u8'):
            return self.send_response(NotFoundResponse())
        # 验证该播放链接是否是该视频的
        vod_video = await VodDao.get_by_vod_id(int(vod_id))
        url_content = vod_video['vod_play_url']
        if play_url not in url_content:
            return self.send_response(NotFoundResponse(msg='没有这条播放链接'))

        current_time_int = int(current_time)
        user_id = 1
        create_time = datetime.datetime.now()
        return_id = await TanmuDao.insert_danmu(vod_id, play_url,  content, current_time, current_time_int, user_id, create_time)
        print(return_id)
        self.send_response(Response({'id': 0}))

