from typing import List

from vo.video_detail_vo import Url


class VideoHandlerMixin:
    @staticmethod
    def _parse_vod_play_url(play_url: str) -> List[Url]:
        if play_url.startswith('http'):
            return [{
                'play_line_name': '播放地址1',
                'links': [{'name': '在线播放', 'link': play_url}]
            }]
        play_group_links = play_url.split('$$$')
        play_group_links_list = []
        for index, links_str in enumerate(play_group_links):
            name_eps = links_str.split('$$')
            links_list = []
            for eps in name_eps:
                for ep in eps.split('#'):
                    name, link = ep.split('$')
                    links_list.append({
                        'name': name,
                        'link': link
                    })
            play_group_links_list.append({
                'play_line_name': '播放地址{}'.format(index + 1),
                'links': links_list
            })
        return play_group_links_list
