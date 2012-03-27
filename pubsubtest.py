from dirigent import pubsub

events = pubsub()

def a(*args, **kwargs):
    print "a:", args, kwargs

def b(*args, **kwargs):
    print "b:", args, kwargs

@events.sub
def c(*args, **kwargs):
    print "c:", args, kwargs

@events.sub
def d(*args, **kwargs):
    print "d:", args, kwargs

events.sub(a)
events.sub(b)

events.pub("Hi!", hello="world!")
