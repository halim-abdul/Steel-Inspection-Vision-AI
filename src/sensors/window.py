from collections import deque

class RollingWindow:
    def __init__(self, size=128):
        self.data=deque(maxlen=size)
    def push(self, value):
        self.data.append(float(value))
    def values(self):
        return list(self.data)
    def ready(self):
        return len(self.data)==self.data.maxlen
