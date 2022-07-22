class LastValueMap:
  def __init__(self):
    self.d = OrderedDict()

  def set(self, key, value):
    self.d[key] = value
    self.d.move_to_end(key)

  def remove(self, key):
    if key in self.d:
      del self.d[key]

  def getLast(self):
    return self.d[next(reversed(self.d))]
