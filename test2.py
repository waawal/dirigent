import dirigent

a = dirigent.notify()

def b(ar=None):
    print ar or "\nhello\n"

a.register(b)

a.notify("yo")


@dirigent.observe(a)
def c(ar, ab="Nogo!"):
    print "c func called", ar, ab

for b in a:
    b("from generator")
wobs = dirigent.notify()

wobs.register(c)

with wobs("asd", ab="GOOOOO!") as hello:
   for g in hello:
        print g
