from dirigent import notify, observe, notification

@observe("test_event")
def print_me(*args, **kwargs):
    print("! print_me called !")
    if "test" in kwargs:
        print("Yep, it's there: ", kwargs["test"])
    return "I returned!"

with notification("test_event", test="Hello there!"):
   print ("I am inside a with statement")

notify("test_event")


def hello():
    return "HELLO!"

notify.register("test_event", hello)

for result in notify("test_event", asgenerator=True):
    print(result.called)

"""
! print_me called !
Yep, it's there:  Hello there!
I am inside a with statement
! print_me called !
<function print_me at 0xb7729a74>
<function hello at 0xb7729a3c>
"""

