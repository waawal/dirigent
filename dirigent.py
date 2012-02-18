from collections import defaultdict, namedtuple


__all__ = "notify", "observe"


class ObserverClass(object):
    """ Object holding all the observers, aliased to notify.
    """
    def __init__(self):
        self.observers = defaultdict(list)
        
    def register(self, name, func):
        """ Register a callback for a event
        """
        self.observers[name].append(func)

    def unregister(self, name, func):
        """ Unregisters a event.
        """
        if name in self.observers and func in self.observers[name]:
            self.observers[name].remove(func)

    def notify(self, name, *args, **kwargs):
        """ Notifies all registered observers of a registered event.
            Returns a list of tuples (called object, result)
        """
        Result = namedtuple('Result', 'called result')

        return [Result(observer, observer(*args, **kwargs)) for observer
                in self.observers[name]]

    __call__ = notify


class NotificationClass(object):
   """ Implements the with-statement.
   """
   def __init__(self, name, before=None, after=None, *args, **kwargs):
       self.name = name
       if before:
           self.before = True
       if after:
           self.after = True
       if not before and not after:
           self.before = True
           
       self.args = args
       self.kwargs = kwargs

   def __enter__(self):
       if self.before:
           notify(self.name, *self.args, **self.kwargs)

   def __exit__(self, exctype, excvalue, traceback):
       if not exctype and not excvalue and not traceback and self.after:
           notify(self.name, *self.args, **self.kwargs) 


def observe(name):
    """ A decorator that makes a function/method to a observer.
    """
    def wrapper(func):
        notify.register(name, func)
        return func
    return wrapper

# aliases
notification = NotificationClass

# Instantiatons
notify = ObserverClass()
