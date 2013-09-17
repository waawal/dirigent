from dirigent.base import BaseSubject
import gevent

class GeventSubject(BaseSubject):

    def notify(self, *args, **kwargs):
        return [gevent.spawn(observer, *args, **kwargs).value for observer in self.observers]

# Alias
Subject = GeventSubject