import tornado.ioloop
import tornado.web
from tornado_request_mapping import Route

from handlers.index_handler import IndexHandler
from handlers.vod_handler import VodHandler


def register_handler(app):
    route = Route(app)
    route.register(IndexHandler)
    route.register(VodHandler)


if __name__ == '__main__':
    app = tornado.web.Application()
    register_handler(app)
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
