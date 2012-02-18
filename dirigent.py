

__all__ = "notify", "observe"

class ObserverClass(object):
    
    _implemented = ("user_created", "user_updated", "user_removed",
                    "group_created", "group_updated", "group_removed",
                    "user_authenticated")
    def __init__(self):
        self.observers = dict((name, []) for name in self._implemented)
        
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
notify = ObserverClass()

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