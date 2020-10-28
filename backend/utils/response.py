from typing import Any


class Response:
    code: int
    msg: str = ''
    data: Any

    def __init__(self, data, code=200):
        self.data = data
        self.code = code

    def to_dict(self):
        return {
            'code': self.code,
            'msg': self.msg,
            'data': self.data
        }
