from typing import List

from models.mac_type import MacType
from utils.db_utils import Select, Update, Insert


class TypeDao:
    @classmethod
    @Select(
        "select type_id, type_name, type_en, type_sort from mac_type where type_pid = %(pid)s order by type_sort asc ")
    async def get_type_by_pid(cls, pid) -> List[MacType]: pass

    @classmethod
    @Select("select type_id from mac_type where type_en = %(type_en)s")
    async def get_by_type_en(cls, type_en: str) -> MacType:
        pass

    @classmethod
    @Select("select * from mac_type order by type_sort asc, type_en  ")
    async def get_all_type(cls) -> List[MacType]: pass

    @classmethod
    # @Update("update test set name = %(type_en)%")
    # .and_('type_id = %(type_id)s', lambda type_id: type_id.split() != '')
    @Insert("insert into mac_tanmu (vod_id, play_url, content, `current_time`, current_time_int, styles, user_id, create_time) "
            "values (%(vod_id)s, %(play_url)s)")
    def test(cls, type_en) -> List[dict]:
        pass
