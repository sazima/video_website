import datetime

from typing_extensions import TypedDict


class Tanmu(TypedDict):
    tanmu_id: int
    vod_id: int
    content: str
    play_url: str
    current_time: float
    current_time_int: int
    styles: str
    user_id: int
    create_time: datetime.datetime
