import datetime
import traceback
import uuid
from collections import defaultdict

from client.collection_client import VideoCollectionClient
from config import Config
from model.tanmu_models import Video, Type, VideoLink
from utils.logger_factory import LoggerFactory


def collection_video(key, hours):
    logger = LoggerFactory.get_logger()
    url = ''
    bind_id_dict = dict()
    for api in Config.api_list:
        if api['key'] == key:
            url = api['url']
            bind_id_dict = api['bind_id']
            break
    if not url:
        raise
    vc = VideoCollectionClient(url)
    api_type_id_to_name = vc.get_type_id_to_toname()
    logger.info(f'所有分类: {api_type_id_to_name}')
    # print(res)
    page = 1
    all_db_type = tanmu_session.query(Type).all()
    id_to_type = {x.id: x for x in all_db_type}
    while True:
        video_list, page_count = vc.get_video_info_by_hours(hours, page)
        logger.info(f'------{page}页/共{page_count}页------')
        name_list = [x['name'] for x in video_list]
        db_video_by_name_list = tanmu_session.query(Video).filter(Video.name.in_(name_list)).all()
        name_to_video = {x.name: x for x in db_video_by_name_list}
        for video in video_list:
            type_id = video['tid']
            if type_id not in bind_id_dict:
                try:
                    logger.info(f'分类未绑定, 跳过, {video["name"]} , 分类名称: {api_type_id_to_name[video["tid"]]}')
                except KeyError:
                    logger.info(f'分类未绑定, 跳过, {video["name"]} , 分类id: {video["tid"]}')
            db_video_by_name = name_to_video.get(video['name'])
            # 当数据库中存储的api更新时间 小于 当前获取到更新过时间， 就更新
            if not db_video_by_name:
                # 创建
                logger.info(f'创建, {video["name"]}')
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
            elif db_video_by_name.api_update_time is None or\
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
                logger.info('更新 ' + video['name'])
            else:
                logger.info('跳过 ' + video['name'])
        page += 1
        if page > page_count:
            break


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, scoped_session
    tanmu_engine = create_engine(Config.sql_url)
    tanmu_session = scoped_session(sessionmaker(bind=tanmu_engine))
    try:
        collection_video('tiankong', 48)
        tanmu_session.commit()
    except Exception:
        tanmu_session.rollback()
        LoggerFactory.get_logger().error(traceback.format_exc())
        raise
