from tornado_request_mapping import request_mapping

from utils.base_handler import BaseHandler


@request_mapping('/user')
class UserHandler(BaseHandler):
    pass
