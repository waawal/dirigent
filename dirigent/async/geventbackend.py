import gevent


from dirigent.base import SubjectBase

class GeventSubject(SubjectBase):

    def notify(self, *args, **kwargs):
        [gevent.spawn(observer, *args, **kwargs) for observer in self.observers]
