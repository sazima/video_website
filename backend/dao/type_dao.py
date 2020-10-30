from typing import List

from models.mac_type import MacType
from utils.db_utils import Select


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
    @Select('select * from mac_type where 1 = 1 ') \
            .and_("type_en = %(type_en)s", lambda type_en: type_en.strip() != '')
    # .and_('type_id = %(type_id)s', lambda type_id: type_id.split() != '')
    def test(cls, type_en) -> List[dict]:
        pass
