from dirigent.base import BaseSubject
import rq

class RQSubject(BaseSubject):

    def notify(self, *args, **kwargs):
        rq.use_connection()
        q = rq.Queue()
        [q.enqueue(observer, *args, **kwargs) for observer in self.observers]

