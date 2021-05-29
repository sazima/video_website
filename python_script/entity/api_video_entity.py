from typing import List

from typing_extensions import TypedDict

from entity.play_link_entity import PlayLinkEntity


class ApiVideoEntity(TypedDict):
    last: int
    id: str
    tid: int
    name: str
    pic: str
    state: str
    play_list: List[PlayLinkEntity]
    des: str

