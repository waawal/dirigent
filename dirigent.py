from collections import defaultdict


__all__ = "notify", "observe"


class ObserverClass(object):
    
    def __init__(self):
        self.observers = defaultdict(list)
        
    def register(self, name, func):
        ''' Register a callback for a event
        '''
        self.observers.setdefault(name, []).append(func)

    def unregister(self, name, func):
        ''' Unregisters a event. '''
        if name in self.observers and func in self.observers[name]:
            self.observers[name].remove(func)

    def notify(self, name, *arg, **kw):
        ''' Notifies all registered observers of an event
        '''
        observers = self.observers[name] # TODO: callables __repr__ with return
        return [observer(*arg, **kw) for observer in observers]

    __call__ = notify


class NotificationClass(object):
   # TODO: Should support *args and *kwargs
   def __init__(self, name, before=None, after=None):
       self.name = name
       if before:
           self.before = True
       if after:
           self.after = True
       if not before and not after:
           self.before = True

   def __enter__(self):
       if self.before:
           notify(self.name)

   def __exit__(self, exctype, excvalue, traceback):
       if not exctype and not excvalue and not traceback and self.after:
           notify(self.name) 


def observe(name):
    """ Returns a Python decorator that attaches a callback to a observer.
    >>> @observe('user_created')
    >>> def hello(*arg):
    >>>     if 34 in arg:
    >>>         print "oh hai there"
    >>> notify('user_created', 34)
    oh hai there
    [None]
    >>> notify('user_created', 35)
    [None]
    """
    def wrapper(func):
        notify.register(name, func)
        return func
    return wrapper

# aliases
notification = NotificationClass

# Instantiatons
notify = ObserverClass()
