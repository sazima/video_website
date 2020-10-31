from typing import List

from typing_extensions import TypedDict


class Link(TypedDict):
    name: str
    link: str


class Url(TypedDict):
    play_line_name: str
    links: List[Link]


class VideoDetailVo(TypedDict):
    vod_id: int
    vod_name: str
    vod_pic: str
    vod_blurb: str
    urls: List[Url]
