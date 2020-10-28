from utils.db_utils import select


class VodDao:
    @classmethod
    @select(
        "select 'vod_pic', 'vod_name', 'vod_time', 'vod_id' from mac_vod "
        "where type_id = %(type_id)s or type_id_1 = %{type_id} order by type_id desc limit %(limit)s "
    )
    async def get_vod_by_type_id(cls, type_id: int, limit: int):
        pass
