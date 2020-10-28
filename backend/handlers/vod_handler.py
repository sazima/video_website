import tornado
from tornado_request_mapping import request_mapping

from utils.base_handler import BaseHandler


@request_mapping("/api/video")
class VodHandler(BaseHandler):

    @request_mapping('/get_list', 'get')
    async def get_list(self):
        type_en = self.get_argument('type_en')
        page = self.get_argument('page')
        per_page = self.get_argument('per_page')

