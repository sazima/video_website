from typing import Any
from datetime import datetime
import json


class Response:
    code: int = 200
    msg: str = ''
    data: Any = None

    def __init__(self, data=None, msg=None, code=None):
        self.data = data
        if code:
            self.code = code
        if msg:
            self.msg = msg

    def to_dict(self) -> dict:
        return {
            'code': self.code,
            'msg': self.msg,
            'data': self.data
        }


class NotFoundResponse(Response):
    code = 404
    msg = '不存在'


class FuckYouResponse(Response):
    code = 405
    msg = 'Fuck you !!!!'


class ErrorResponse(Response):
    code = 406
    msg = '出错啦 !!!!'


class _DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)
