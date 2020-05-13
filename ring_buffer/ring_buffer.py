class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def append(self, item):
        if len(item) > 1:
            
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        elif len(self.storage) > 0:
            self.storage.remove(self.storage[0])
            self.storage.append(item)

    def get(self):
        return self.storage