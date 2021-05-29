import datetime
from typing import Tuple, List, Dict

import requests
import xmltodict

from entity.api_video_entity import ApiVideoEntity


class VideoCollectionClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.index_url = self.base_url
        self.video_info_list_url = base_url + '?ac=videolist&t=&pg=&h={hours}&ids=&wd=&pg={page}'

    def get_type_id_to_toname(self) -> Dict[int, str]:
        response = requests.get(self.index_url)
        o = xmltodict.parse(response.text)
        type_id_to_name = {int(x['@id']): x['#text'] for x in o['rss']['class']['ty']}
        return type_id_to_name

    def get_video_info_by_hours(self, hours: int, page=1) -> Tuple[List[ApiVideoEntity], int]:
        url = self.video_info_list_url.format(hours=hours, page=page)
        response = requests.get(url)
        o = xmltodict.parse(response.text)
        vide_list = o['rss']['list']['video']
        # size = o['rss']['list']['@pagesize']
        page_count = o['rss']['list']['@pagecount']
        return_list = list()  # type: List[ApiVideoEntity]
        for video in vide_list:
            last = int(datetime.datetime.strptime(video['last'], '%Y-%m-%d %H:%M:%S').timestamp())
            item = {
                'last': last,
                'id': video['id'],
                'tid': int(video['tid']),
                'name': video['name'],
                'pic': video['pic'],
                'state': video['state'],
                'des': video['des'],
                'play_list': list()
            }  # type: ApiVideoEntity
            play_list = []
            # player_name_to_name_url_dict = dict()   # type: Dict[str, List[PlayLinkEntity]]
            player_name = video['dl']['dd']['@flag']
            # player_name_to_name_url_dict[player_name] = []
            text = video['dl']['dd']['#text']
            name_url_list = text.split('#')
            for name_url in name_url_list:
                name, url = name_url.split('$')
                play_list.append({
                    'name': name,
                    'url': url,
                    'player_name': player_name
                })
            item['play_list'] = play_list
            return_list.append(item)
        return return_list, int(page_count)

