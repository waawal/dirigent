from collections import defaultdict
from functools import wraps

__all__ = "notify", "observe"


class ObserverClass(object):
    """ Object holding all the observers, aliased to notify.
    """
    def __init__(self):
        self.observers = set()
        self.contextargs = (tuple(), {})

    def register(self, func):
        """ Register a callback for a event
        """
        self.observers.add(func)

    def unregister(self, func):
        """ Unregisters a event.
        """
        if func in self.observers:
            self.observers.remove(func)

    def notify(self, *args, **kwargs):
        """ Notifies all registered observers of a registered event.
            Returns a list of tuples (called object, result)
        """
        return [observer(*args, **kwargs) for observer in self.observers]

    def __iter__(self):
        return (observer for observer in self.observers)

    def __enter__(self):
        return self.__iter__()

    def __exit__(self, exctype, excvalue, traceback):
        if not exctype and not excvalue and not traceback:
            args, kwargs = self.contextargs
            self.contextargs = (tuple(), {})
            return self.notify(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if args and kwargs:
            self.contextargs = (args or None, kwargs or {})
        elif args:
            self.contextargs = (args, {})
        elif kwargs:
            self.contextargs = (tuple(), kwargs)
        return self

def observe(name):
    """ A decorator that makes a function/method to a observer.
    """
    def wrapper(func):
        @wraps(func)
        name.register(func)
        return func
    return wrapper

def notification(name, *args, **kwargs):
    yield
    name.notify(*args, **kwargs)


# aliases
notify = ObserverClass
