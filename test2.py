import dirigent

a = dirigent.subject()
def b(ar=None, **kwargs):
    print ar or "\nhello\n"
    print kwargs

a.register(b)

a.notify("yo")


@dirigent.observe(a)
def c(ar, ab="Nogo!", **kwargs):
    print "c func called", ar, ab

for b in a:
    b("from generator")

wobs = dirigent.subject()

wobs.register(c)
wobs.register(b)

with dirigent.notification(wobs, "from contextmanager",after=True,  ab="GOOOOO!", l="ol") as hello:
   for g in hello:
        g(cat="mouse")
   #print "in block"
