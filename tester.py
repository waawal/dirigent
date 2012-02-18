from dirigent import notify, observe, notification

@observe("test_event")
def print_me(*args, **kwargs):
    print "! print_me called !"
    if "test" in kwargs:
        print "Yep, it's there: ", kwargs["test"]
    return "I returned!"

with notification("test_event", test="Hello there!"):
   print "I am inside a with statement"

notify("test_event")
