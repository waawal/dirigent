from dirigent.base import BaseSubject

class HardRefSubject(BaseSubject):

    def __init__(self, init):
        self.observers = set(init)
