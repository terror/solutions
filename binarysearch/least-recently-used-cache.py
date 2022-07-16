class LRUCache:
    def __init__(self, capacity):
      self.store = OrderedDict()
      self.capacity = capacity

    def get(self, key):
      if key not in self.store:
        return -1
      self.store.move_to_end(key)
      return self.store[key]

    def set(self, key, val):
      self.store[key] = val
      self.store.move_to_end(key)
      if len(self.store) > self.capacity:
        self.store.popitem(last = False)
