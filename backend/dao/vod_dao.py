from typing import List

from models.mac_vod import MacVod
from utils.db_utils import select


class VodDao:
    @classmethod
    @select(
        "select vod_pic, vod_name, vod_time, vod_id from mac_vod "
        "where type_id = %(type_id)s or type_id_1 = %(type_id)s order by vod_id desc limit %(limit)s "
    )
    async def get_index_vod_by_type_id(cls, type_id: int, limit: int) -> List[dict]:
        pass

    @classmethod
    @select(
        "select * from mac_vod "
        "where type_id = %(type_id)s or type_id_1 = %(type_id)s order by vod_id desc limit %(start)s, %(limit)s"
    )
    async def get_vod_by_type_id(cls, type_id: int, start: int, limit: int) -> List[MacVod]:
        pass

    @classmethod
    @select("select count(0) from mac_vod where type_id =  %(type_id)s or type_id_1 = %(type_id)s ")
    async def get_count_by_type_id(cls, type_id: int) -> int:
        pass

    @classmethod
    @select("select * from mac_vod where vod_id = %(vod_id)s ")
    async def get_by_vod_id(cls, vod_id: int) -> MacVod:
        pass
