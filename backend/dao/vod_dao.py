from typing import List

from models.mac_vod import MacVod
from utils.db_utils import select


# 视频
class VodDao:

    @classmethod
    @select(
        "select * from mac_vod "
        "where type_id = %(type_id)s or type_id_1 = %(type_id)s order by vod_id desc limit %(limit)s "
    )
    async def get_index_video_by_type_id(cls, type_id: int, limit: int) -> List[MacVod]:
        pass

    @classmethod
    @select(
        "select * from mac_vod "
        "where type_id = %(type_id)s or type_id_1 = %(type_id)s order by vod_id desc limit %(start)s, %(limit)s"
    )
    async def get_video_by_type_id(cls, type_id: int, start: int, limit: int) -> List[MacVod]:
        pass

    @classmethod
    @select("select count(0) from mac_vod where type_id =  %(type_id)s or type_id_1 = %(type_id)s ")
    async def get_count_by_type_id(cls, type_id: int) -> int:
        pass

    @classmethod
    @select("select * from mac_vod where vod_id = %(vod_id)s ")
    async def get_by_vod_id(cls, vod_id: int) -> MacVod:
        pass

    # 获取轮播图
    @classmethod
    @select("select * from mac_vod where vod_level = 9")
    async def get_brand_video(cls) -> List[MacVod]:
        pass


