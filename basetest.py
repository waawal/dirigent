from dirigent import Subject
import random
import time

events = Subject()

@events.register
def a(*args, **kwargs):
    print "a:", args[0], kwargs
    time.sleep(random.randint(0,2))
    print "returned: a", args[0] 

@events.register
def b(*args, **kwargs):
    print "b:", args[0], kwargs
    time.sleep(random.randint(0,2))
    print "returned: b", args[0] 

@events.register
def c(*args, **kwargs):
    print "c:", args[0], kwargs
    time.sleep(random.randint(0,2))
    print "returned: c", args[0] 

@events.register
def d(*args, **kwargs):
    print "d:", args[0], kwargs
    time.sleep(random.randint(0,2))
    print "returned: d", args[0]


for i, _ in enumerate(xrange(2)):
    events.notify(i, hello="world!")
    print "Moving on..."
print "done!"
