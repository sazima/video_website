from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    request: HTTPServerRequest

    def data_received(self, chunk):
        pass


    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Allow-Methods', '*')
