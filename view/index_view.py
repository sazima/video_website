from tornado_request_mapping import request_mapping
from tornado.web import RequestHandler


@request_mapping('/')
class IndexView(RequestHandler):

    @request_mapping('/index.html')
    async def get_index(self):
        self.render('index.html', title='test')
