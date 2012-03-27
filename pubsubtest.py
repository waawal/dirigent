from dirigent import pubsub

q = pubsub()

def a(*args, **kwargs):
    print "a:", args, kwargs

def b(*args, **kwargs):
    print "b:", args, kwargs

@q.sub
def c(*args, **kwargs):
    print "c:", args, kwargs

@q.sub
def d(*args, **kwargs):
    print "d:", args, kwargs

q.sub(a)
q.sub(b)

q.pub("hello", world="sa")
