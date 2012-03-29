from dirigent.async.geventbackend import GeventSubject
import gevent
import random


events = GeventSubject()

@events.register
def a(*args, **kwargs):
    print "a:", args, kwargs
    gevent.sleep(random.randint(0,2))
    print "returned: a", args[0] 

@events.register
def b(*args, **kwargs):
    print "b:", args, kwargs
    gevent.sleep(random.randint(0,2))
    print "returned: b", args[0] 

@events.register
def c(*args, **kwargs):
    print "c:", args, kwargs
    gevent.sleep(random.randint(0,2))
    print "returned: c", args[0] 

@events.register
def d(*args, **kwargs):
    print "d:", args, kwargs
    gevent.sleep(random.randint(0,2))
    print "returned: d", args[0]


for i, _ in enumerate(xrange(5)):
    events.notify(i, hello="world!")
    print "Moving on..."
    gevent.sleep(1)
gevent.sleep(3)
