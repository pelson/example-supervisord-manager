import logging
import os

import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.process
import tornado.log


update_script = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                             'update.sh')


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        logging.info('About to start the update process.')
        self.write("Working...<br>")
        self.flush()
        proc = tornado.process.Subprocess([update_script])
        yield proc.wait_for_exit()
        self.write("Daemon updated")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    app = make_app()
    app.listen(8888)
    loop = tornado.ioloop.IOLoop.current()
    loop.start()
