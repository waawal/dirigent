from dirigent.base import BaseSubject

class RQSubject(BaseSubject):

	def __init__(self, queue):
		BaseSubject.__init__()
		self.q = queue

    def notify(self, *args, **kwargs):
        [self.q.enqueue(observer, *args, **kwargs)
         for observer in self.observers]

# Alias
Subject = RQSubject
