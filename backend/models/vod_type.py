from typing_extensions import TypedDict


class VodType(TypedDict, total=False):
    type_id: int
    type_name: str
    type_en: str
    type_sort: int
    type_mid: int
    type_pid: int
    type_status: int
    type_tpl: str
    type_tpl_list: str
    type_tpl_detail: str
    type_tpl_play: str
    type_tpl_down: str
    type_key: str
    type_des: str
    type_title: str
    type_union: str
    type_extend: str
    type_logo: str
    type_pic: str
    type_jumpurl: str

