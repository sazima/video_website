import datetime

from typing_extensions import TypedDict


class VodListVo(TypedDict):
    vod_id: int
    vod_name: str
    vod_time: datetime.datetime
    vod_pic: str
