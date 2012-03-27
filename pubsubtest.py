from dirigent import subject

q = subject()

def a(*args, **kwargs):
    print "a:", args, kwargs

def b(*args, **kwargs):
    print "b:", args, kwargs

@q.observe
def c(*args, **kwargs):
    print "c:", args, kwargs

def d(*args, **kwargs):
    print "d:", args, kwargs

q.register(a)
q.register(b)

q.notify("hello", world="sa")
