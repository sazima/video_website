import datetime

from typing_extensions import TypedDict


class Tanmu(TypedDict, total=False):
    tanmu_id: int
    vod_id: int
    content: str
    play_url: str
    play_name: str  # 当前链接名称,比如bd高清
    vod_play_from: str
    current_time: float
    current_time_int: int
    styles: str
    user_id: int
    create_time: datetime.datetime
