from contextlib import contextmanager
from functools import partial
import pdb
__all__ = ("subject",
           "observe",
           "notification",
           "notification_before",
           "notification_after")

class SubjectBase(object):
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
        """
        return [observer(*args, **kwargs) for observer in self.observers]

    def __iter__(self):
        return (observer for observer in self.observers)
        
    def __call__(self, *args, **kwargs):
        return (partial(observer, *args, **kwargs) for observer in self.observers)

    def observe(self, func):
        """ A decorator that registers a function/method as a observer to a subject.
        """
        self.register(func) 
        return func   

    # Aliases
    sub = subscribe = register
    notify_listeners = pub = publish = notify


@contextmanager
def notification(subject, *args, **kwargs):
    try:
        yield subject(*args, **kwargs)
    finally:
        pass

@contextmanager
def notification_before(subject, *args, **kwargs):
    try:
        subject.notify(*args, **kwargs)
        yield
    finally:
        pass

@contextmanager
def notification_after(subject, *args, **kwargs):
    try:
        yield
    finally:
        subject.notify(*args, **kwargs)

     
# Aliases
subject = SubjectBase
SubjectBase.observers = notification
SubjectBase.before = notification_before
SubjectBase.after = notification_after
