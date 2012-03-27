from contextlib import contextmanager
from functools import wraps, partial

__all__ = "notify", "observe"


class ObserverClass(object):
    """ Object holding all the observers, aliased to notify.
    """
    def __init__(self):
        self.observers = set()

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
        
    def __call__(self, *args, **kwargs):
        return (partial(observer, *args, **kwargs) for observer in self.observers)

def observe(name):
    """ A decorator that makes a function/method to a observer.
    """
    #@wraps(name)
    def wrapper(func):
        name.register(func)
        return func
    return wrapper

@contextmanager
def notification(name, *args, **kwargs):
    try:
        yield name(*args, **kwargs)
    finally:
        pass

@contextmanager
def notification_before(name, *args, **kwargs):
    try:
        name.notify(*args, **kwargs)
        yield
    finally:
        pass

@contextmanager
def notification_after(name, *args, **kwargs):
    try:
        yield
    finally:
        name.notify(*args, **kwargs)
                                    


# aliases
notify = ObserverClass
