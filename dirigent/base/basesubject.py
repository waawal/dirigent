from functools import partial
try:
    from weakref import WeakSet
except ImportError:
    from dirigent.contrib.weakrefset import WeakSet


class BaseSubject(object):
    """ Object holding all the observers, aliased to notify.
    """
    def __init__(self, init):
        self.observers = WeakSet(init)

    def register(self, func):
        """ Register a callback for a event
        Can be used as a decorator.
        """
        self.observers.add(func)
        return func

    def unregister(self, func):
        """ Unregisters a event.
        """
        if func in self.observers:
            self.observers.remove(func)

    def notify(self, *args, **kwargs):
        """ Notifies all registered observers of a registered event.
        """
        [observer(*args, **kwargs) for observer in self.observers]

    def __iter__(self):
        return (observer for observer in self.observers)

    def __call__(self, *args, **kwargs):
        return (partial(observer, *args, **kwargs) for observer in self.observers)
