from tornado_request_mapping import request_mapping

from utils.base_handler import BaseHandler


@request_mapping('/api/user')
class UserHandler(BaseHandler):
    @request_mapping("/register", method='post')
    def register(self):
        user_name = self.data.get('user_name')
        user_pwd = self.data.get('user_pwd')
        user_email = self.data.get('user_email')
