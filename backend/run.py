import tornado.ioloop
import tornado.web
from tornado_request_mapping import request_mapping, Route

from handlers.index_handler import IndexHandler


@request_mapping("/test")
class MainHandler(tornado.web.RequestHandler):

    @request_mapping('/', method='get')
    async def test(self):
        self.write("Hello, world. get")


def register_handler(app):
    route = Route(app)
    route.register(MainHandler)
    route.register(IndexHandler)


if __name__ == '__main__':
    app = tornado.web.Application()
    register_handler(app)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
