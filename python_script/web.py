import datetime
import json
import traceback
import uuid
from collections import defaultdict

import tornado.ioloop
import tornado.web
from sqlalchemy.orm import scoped_session, sessionmaker
from tornado_request_mapping import request_mapping, Route

from client.collection_client import VideoCollectionClient
from config import Config
from model.tanmu_models import ThirdApi, Type, Video, VideoLink
from utils.logger_factory import LoggerFactory
from threading import Thread, Lock
lock = Lock()


@request_mapping("/api/collectionVideo")
class MainHandler(tornado.web.RequestHandler):
    _key_to_task_info = defaultdict(list)

    @request_mapping('/start_task', method='get')
    async def test(self):
        key = self.get_argument("key", "")  #
        hour = int(self.get_argument("hours", '24'))
        if lock.locked():
            LoggerFactory.get_logger().info('正在执行')
            return self.write({})
        t = Thread(target=self._do_collection_video_task, args=(key, hour))
        t.start()
        self.write({})

    @request_mapping("/get_task_by_key")
    async def get_task_by_key(self):
        key = self.get_argument("key", "")  #
        if key in self._key_to_task_info:
            result = self._key_to_task_info[key]
        else:
            result = []
        self.write({
            'data': result
        })

    def _do_collection_video_task(self, key, hours):
        lock.acquire(timeout=5)
        logger = LoggerFactory.get_logger()
        tanmu_session = scoped_session(sessionmaker(bind=Config.tanmu_engine))
        try:
            self._key_to_task_info[key] = [datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            third_api_entity = tanmu_session.query(ThirdApi).filter(ThirdApi.key == key).first()
            if not third_api_entity:
                msg = '该 key 不存在'
                logger.info(msg)
                self._key_to_task_info[key].append(msg)
                return
            _bind_id = json.loads(third_api_entity.bind_id)
            bind_id_dict = {x['apiId']: x['systemId'] for x in _bind_id}
            vc = VideoCollectionClient(third_api_entity.url)
            api_type_id_to_name = vc.get_type_id_to_toname()
            msg = f'所有分类: {api_type_id_to_name}'
            logger.info(msg)
            self._key_to_task_info[key].append(msg)
            # print(res)
            page = 1
            all_db_type = tanmu_session.query(Type).all()
            id_to_type = {x.id: x for x in all_db_type}
            while True:
                video_list, page_count = vc.get_video_info_by_hours(hours, page)
                msg = f'------{page}页/共{page_count}页------'
                logger.info(msg)
                self._key_to_task_info[key].append(msg)
                name_list = [x['name'] for x in video_list]
                db_video_by_name_list = tanmu_session.query(Video).filter(Video.name.in_(name_list)).all()
                name_to_video = {x.name: x for x in db_video_by_name_list}
                for video in video_list:
                    type_id = video['tid']
                    if type_id not in bind_id_dict:
                        try:
                            msg = f'分类未绑定, 跳过, {video["name"]} , 分类名称: {api_type_id_to_name[video["tid"]]}'
                        except KeyError:
                            msg = f'分类未绑定, 跳过, {video["name"]} , 分类id: {video["tid"]}'
                        logger.info(msg)
                        self._key_to_task_info[key].append(msg)
                        continue
                    db_video_by_name = name_to_video.get(video['name'])
                    # 当数据库中存储的api更新时间 小于 当前获取到更新过时间， 就更新
                    if not db_video_by_name:
                        # 创建
                        msg = f'创建, {video["name"]}'
                        insert_video = Video()
                        insert_video.type_id1 = bind_id_dict[type_id]
                        insert_video.type_id2 = id_to_type[bind_id_dict[type_id]].parent_type
                        insert_video.name = video['name']
                        insert_video.picture = video['pic']
                        insert_video.content = video['des']
                        insert_video.av = uuid.uuid4().hex
                        insert_video.update_time = int(datetime.datetime.now().timestamp())
                        insert_video.api_update_time = video['last']
                        tanmu_session.add(insert_video)
                        tanmu_session.flush()
                        insert_player_list = []
                        for play in video['play_list']:
                            video_link = VideoLink()
                            video_link.video_id = insert_video.id
                            video_link.play_url = play['url']
                            video_link.play_name = play['name']
                            video_link.from_name = play['player_name']
                            insert_player_list.append(video_link)
                        tanmu_session.bulk_save_objects(insert_player_list)
                    elif db_video_by_name.api_update_time is None or \
                            db_video_by_name.api_update_time < video['last']:
                        # 更新
                        tanmu_session.query(Video).filter(Video.id == db_video_by_name.id).update({
                            'name': video['name'],
                            'picture': video['pic'],
                            'content': video['des'],
                            'update_time': int(datetime.datetime.now().timestamp()),
                            'api_update_time':  video['last']
                        })
                        new_player_to_name = defaultdict(list)
                        for play in video['play_list']:
                            # 根据 播放器和名称查询， 有则修改， 无则更新， 该播放器不存在的视频名字将删除
                            video_link = tanmu_session.query(VideoLink).filter(VideoLink.video_id==db_video_by_name.id,
                                                                               VideoLink.from_name == play['player_name'],
                                                                               VideoLink.play_name == play['name']).first()
                            if not video_link:
                                video_link = VideoLink()
                                video_link.video_id = db_video_by_name.id
                            video_link.play_url = play['url']
                            video_link.play_name = play['name']
                            video_link.from_name = play['player_name']
                            tanmu_session.add(video_link)
                            tanmu_session.flush()
                            new_player_to_name[play['player_name']].append(play['name'])
                        for player_name, name_list in new_player_to_name.items():  # 删除该播放器旧的播放链接
                            tanmu_session.query(VideoLink).filter(VideoLink.video_id==db_video_by_name.id,
                                                                  VideoLink.from_name == player_name,
                                                                  VideoLink.play_name.notin_(name_list)).delete()
                        msg = '更新 ' + video['name']
                    else:
                        msg = '跳过 ' + video['name']
                    logger.info(msg)
                    self._key_to_task_info[key].append(msg)
                page += 1
                if page > page_count:
                    break
            logger.info('完成')
            self._key_to_task_info[key].append('完成')
            tanmu_session.commit()
        except Exception:
            tanmu_session.rollback()
            logger.error(traceback.format_exc())
            raise
        finally:
            lock.release()


if __name__ == "__main__":
    app = tornado.web.Application()

    route = Route(app)
    route.register(MainHandler)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()