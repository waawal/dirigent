""" Hardref implementation"""
from dirigent.base import BaseSubject


class HardRefSubject(BaseSubject):
    """ Instances implemented with this class will not be based on the default
        weakref implementation.
    """
    def __init__(self, init=None):
        """ Passing a iterable with callables will be used to initialize
            values.
        """
        if init:
            self.observers = set(init)
        else:
            self.observers = set()

