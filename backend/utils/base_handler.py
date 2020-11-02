import json
from decimal import Decimal
from typing import Optional, Awaitable

from tornado.escape import utf8
import datetime
from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler

from utils.response import Response


class BaseHandler(RequestHandler):

    request: HTTPServerRequest

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header("Access-Control-Allow-Methods", "DELETE, POST, GET, OPTIONS")
        self.set_header("Access-Control-Allow-Headers",
                        "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")

    def send_response(self, response: Response):
        response_dict = response.to_dict()
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        chunk = json.dumps(response_dict, cls=_JSONTimeEncoder)
        chunk = utf8(chunk)
        return self._write_buffer.append(chunk)

    def get_remote_ip(self):
        return self.request.headers.get("X-Real-IP") or \
               self.request.headers.get("X-Forwarded-For") or \
               self.request.remote_ip


class _JSONTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(o, Decimal):
            return float(o)
        return json.JSONEncoder.default(self, o)
