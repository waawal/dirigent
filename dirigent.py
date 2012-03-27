from collections import defaultdict


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


class NotificationClass(object):
    """ Implements the with-statement.
    """
    def __init__(self, name, before=False, after=False, *args, **kwargs):
        self.name = name
        self.before = self.after = False # Possible bug?
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
            self.name.notify(*self.args, **self.kwargs)

    def __exit__(self, exctype, excvalue, traceback):
        if not exctype and not excvalue and not traceback and self.after:
            self.name.notify(*self.args, **self.kwargs)


def observe(name):
    """ A decorator that makes a function/method to a observer.
    """
    def wrapper(func):
        name.register(func)
        return func
    return wrapper


# aliases
notification = NotificationClass
notify = ObserverClass
