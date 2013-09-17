from ..base import BaseSubject
import gevent

class GeventSubject(BaseSubject):

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            gevent.spawn(observer, *args, **kwargs)

# Alias
Subject = GeventSubject