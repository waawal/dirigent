from dirigent import pubsub, GeventSubject
import gevent
import random


events = GeventSubject()

def a(*args, **kwargs):
    print "a:", args, kwargs
    gevent.sleep(random.randint(0,2))
    print "a:"

def b(*args, **kwargs):
    print "b:", args, kwargs
    gevent.sleep(random.randint(0,2))
    print "b:"

@events.sub
def c(*args, **kwargs):
    print "c:", args, kwargs
    gevent.sleep(random.randint(0,2))
    print "c:"

@events.sub
def d(*args, **kwargs):
    print "d:", args, kwargs
    gevent.sleep(random.randint(0,2))
    print "d:"

events.sub(a)
events.sub(b)

events.pub("Hi!", hello="world!")
