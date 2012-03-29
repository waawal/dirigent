from dirigent.base import BaseSubject

class HardRefSubject(BaseSubject):

    def __init__(self, init=None):
        if init:
            self.observers = set(init)
        else:
            self.observers = set()

