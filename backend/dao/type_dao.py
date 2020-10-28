from typing import List

from models.vod_type import VodType
from utils.db_utils import DBUtils, select


class TypeDao:
    @classmethod
    @select("select type_id, type_name, type_en, type_sort from mac_type where type_pid = %(pid)s order by type_sort asc ")
    async def get_type_by_pid(cls, pid) -> List[VodType]: pass

    @classmethod
    @select("select * from user where user_name = %(user_name)s")
    async def test(cls, user_name) -> dict: pass
