from dirigent.base import SubjectBase
import tornado.gen
#import tornado.web


class TornadoSubject(SubjectBase):

#    def __init__(self, io_loop=None):
#        self.io_loop = io_loop or tornado.ioloop.IOLoop.instance()

    #@tornado.web.asynchronous
    @tornado.gen.engine
    def notify(self, *args, **kwargs):
        yield [tornado.gen.Task(observer, *args, **kwargs) for observer in self.observers]

    def callback(self, result):
        pass

