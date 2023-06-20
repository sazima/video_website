import os

import tornado
from tornado_request_mapping import Route

from view.index_view import IndexView

if __name__ == "__main__":
    app = tornado.web.Application(
        static_path=os.path.join(os.path.dirname(__file__), "template/static"),
        template_path=os.path.join(os.path.dirname(__file__), "template"),
    )

    route = Route(app)
    route.register(IndexView)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
