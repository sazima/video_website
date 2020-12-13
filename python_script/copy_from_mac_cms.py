import uuid
from typing import Sequence
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from video_models import MacVod, MacType
from tanmu_models import Video, VideoLink, Type

# cms 数据库
cms_engine = create_engine('mysql+pymysql://root:123@127.0.0.1:13306/video')
# 弹幕应用数据库
tanmu_engine = create_engine('mysql+pymysql://root:123@127.0.0.1:13306/tanmu_video')
cms_Session = scoped_session(sessionmaker(bind=cms_engine))
tanmu_session = scoped_session(sessionmaker(bind=tanmu_engine))


def copy_type():
    tanmu_session.query(Type).delete()
    all_type = cms_Session.query(MacType).all()  # type: Sequence[MacType]
    for t in all_type:
        type_ = Type()
        type_.name = t.type_name
        type_.id = t.type_id
        type_.parent_type = t.type_pid
        type_.sort = t.type_sort
        tanmu_session.add(type_)
        tanmu_session.commit()
    print('success copy type')


def mac_cms_to_tanmu_sring():
    latest_video = tanmu_session.query.filter(Video).order_by(Video.update_time.desc()).first()  # type: Video  # 最新的视频
    if latest_video:
        start_time = latest_video.update_time
    else:
        start_time = 1

    all_videos = cms_Session.query(MacVod).filter(MacVod.vod_time > start_time).all()  # type:  Sequence[MacVod]
    total = cms_Session.query(MacVod).filter(MacVod.vod_time > start_time).count()
    count = 0
    insert_objects = []
    for v in all_videos:
        count += 1
        print(f"{count}/{total}, {v.vod_name}")
        tanmu_video = tanmu_session.query(Video).filter(Video.id == v.vod_id).first()  # type: Video
        if tanmu_video:
            print(f"exists")
            if tanmu_video.update_time == v.vod_time:
                print(f"continue")
                continue
            else:
                tanmu_session.query(VideoLink).filter(VideoLink.video_id == v.vod_id).delete()
        else:
            tanmu_video = Video()
            tanmu_video.id = v.vod_id
            tanmu_video.av = uuid.uuid4().hex
        tanmu_video.type_id1 = v.type_id
        tanmu_video.type_id2 = v.type_id_1
        tanmu_video.name = v.vod_name
        tanmu_video.picture = v.vod_pic
        tanmu_video.content = v.vod_content
        tanmu_video.update_time = v.vod_time
        # 播放链接
        parsed = _parse_vod_play_url(v.vod_play_url, v.vod_play_from)
        for item in parsed:
            vod_play_from = item.get('vod_play_from')
            links = item.get('links')
            for link in links:
                name = link.get('name')
                url = link.get('url')
                if len(url) > 254:
                    continue
                video_link = VideoLink()
                video_link.play_url = url
                video_link.play_name = name
                video_link.from_name = vod_play_from
                video_link.video_id = v.vod_id
                insert_objects.append(video_link)
        insert_objects.append(tanmu_video)
        if len(insert_objects) > 10000:
            tanmu_session.bulk_save_objects(insert_objects)
            tanmu_session.commit()
            insert_objects = list()
    if insert_objects:
        tanmu_session.bulk_save_objects(insert_objects)
        tanmu_session.commit()


def _parse_vod_play_url(play_url: str, vod_play_from: str):
    vod_play_from_list = vod_play_from.split('$$$')

    if play_url.startswith('http'):
        return [{
            'play_line_name': '播放地址1',
            'vod_play_from': vod_play_from_list[0],
            'links': [{'name': '在线播放', 'url': play_url}]
        }]

    play_group_links = play_url.split('$$$')
    play_group_links_list = []
    for index, links_str in enumerate(play_group_links):
        name_eps = links_str.split('$$')
        links_list = []  # type: List[Link]
        for eps in name_eps:
            for ep in eps.split('#'):
                if '$' in ep:
                    name, url = ep.split('$')
                else:
                    name, url = '第一集', ep
                links_list.append({
                    'name': name,
                    'url': url
                })
        play_group_links_list.append({
            'play_line_name': '播放地址{}'.format(index + 1),
            'vod_play_from': vod_play_from_list[index],
            'links': links_list
        })
    return play_group_links_list


if __name__ == '__main__':
    copy_type()
    mac_cms_to_tanmu_sring()
