import dirigent

a = dirigent.notify()

def b(ar=None):
    print ar or "\nhello\n"

a.register(b)

for b in a:
    b("homer!")

@dirigent.observe(a)
def c(ar):
    print "c func called", ar

a.notify("yo")
