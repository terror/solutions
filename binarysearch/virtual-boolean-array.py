class BooleanArray:
    def __init__(self):
      self.d = defaultdict(bool)

    def setTrue(self, i):
      self.d[i] = True

    def setFalse(self, i):
      self.d[i] = False

    def setAllTrue(self):
      self.d = defaultdict(lambda: True)

    def setAllFalse(self):
      self.d = defaultdict(bool)

    def getValue(self, i):
      return self.d[i]
