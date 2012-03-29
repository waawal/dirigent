from dirigent.base import BaseSubject
import gevent

class GeventSubject(BaseSubject):

    def notify(self, *args, **kwargs):
        [gevent.spawn(observer, *args, **kwargs) for observer in self.observers]
