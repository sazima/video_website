import datetime
from typing import Tuple, List, Dict

import requests
import xmltodict

from entity.api_video_entity import ApiVideoEntity


class VideoCollectionClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.index_url = self.base_url + '?ac=list'
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
        # import ipdb; ipdb.set_trace()
        if 'video' not in o['rss']['list']:
            video_list = []
        else:
            video_list = o['rss']['list']['video']
        if isinstance(video_list, dict):
            video_list = [video_list]
        page_count = o['rss']['list']['@pagecount']
        return_list = list()  # type: List[ApiVideoEntity]
        for video in video_list:
            if ':' in video['last']:
                last = int(datetime.datetime.strptime(video['last'], '%Y-%m-%d %H:%M:%S').timestamp())
            else:
                last = int(datetime.datetime.strptime(video['last'], '%Y-%m-%d').timestamp())
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
            # player_name_to_name_url_dict = dict()   # type: Dict[str, List[PlayLinkEntity]]
            dd = video['dl']['dd']
            if isinstance(dd, dict):
                dd = [dd]
            play_list = []
            for d in dd:
                player_name = d['@flag']
                text = d['#text']
                name_url_list = text.split('#')
                for name_url in name_url_list:
                    if not name_url:
                        continue
                    name, url, *_ = name_url.split('$')
                    play_list.append({
                        'name': name,
                        'url': url,
                        'player_name': player_name
                    })
            item['play_list'] = play_list
            return_list.append(item)
        return return_list, int(page_count)



if __name__ == '__main__':
    url = 'http://api.leduozy.com/inc/api.php'
    url = 'https://www.ugvapi.com/inc/zyapimac.php'
    vc = VideoCollectionClient(url)
    res = vc.get_video_info_by_hours(24, 1)
    print(res)


