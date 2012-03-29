from dirigent import TornadoSubject
import random
import time

events = TornadoSubject()

@events.register
def a(*args, **kwargs):
    print "a:", args, kwargs
    time.sleep(random.randint(0,2))
    print "returned: a", args[0] 

@events.register
def b(*args, **kwargs):
    print "b:", args, kwargs
    time.sleep(random.randint(0,2))
    print "returned: b", args[0] 

@events.register
def c(*args, **kwargs):
    print "c:", args, kwargs
    time.sleep(random.randint(0,2))
    print "returned: c", args[0] 

@events.register
def d(*args, **kwargs):
    print "d:", args, kwargs
    time.sleep(random.randint(0,2))
    print "returned: d", args[0]


for i, _ in enumerate(xrange(5)):
    events.notify(i, hello="world!")
    print "Moving on..."
    time.sleep(1)
print "waiting..."
time.sleep(3)
print "done!"
