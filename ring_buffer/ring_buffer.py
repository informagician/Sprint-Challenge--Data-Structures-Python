class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.i = 0

    def append(self, item):

        if len(self.storage) < self.capacity:
            self.storage.insert(self.i,item)
            self.i += 1
        elif len(self.storage) == self.capacity:
            self.i = self.i % self.capacity
            self.storage.pop(self.i)
            self.storage.insert(self.i,item)
            self.i += 1

    def get(self):
        return self.storage