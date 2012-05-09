""" The default Subject-class based on a WeakSet storage. """
try:
    from weakref import WeakSet
except ImportError:
    from dirigent.contrib.weakrefset import WeakSet


class BaseSubject(object):
    """ Object holding all the observers, aliased to dirigent.subject
    """
    def __init__(self, init=None):
        if init:
            self.observers = WeakSet(init)
        else:
            self.observers = WeakSet()

    def register(self, func):
        """ Registers a callable.
            Can be used as a decorator.
        """
        self.observers.add(func)
        return func

    def unregister(self, func):
        """ Unregisters a callable.
        """
        if func in self.observers:
            self.observers.remove(func)

    def notify(self, *args, **kwargs):
        """ Notifies all registered observers of an event.
        """
        [observer(*args, **kwargs) for observer in self.observers]

    def __iter__(self):
        return (observer for observer in self.observers)

    __call__ = notify
