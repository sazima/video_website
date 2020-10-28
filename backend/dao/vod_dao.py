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
    @select("select * from mac_vod where type_en =  %(type_en)s order by vod_id desc offset start, limit")
    async def get_vod_by_type_en(cls, type_en: str, start: int, limit: int) -> List[MacVod]:
        pass
