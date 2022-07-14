class PeekableIterator:
    def __init__(self, nums):
      self.nums = nums
      self.pointer = 0

    def peek(self):
      return self.nums[self.pointer]

    def next(self):
      ret = self.nums[self.pointer]
      self.pointer += 1
      return ret

    def hasnext(self):
      return len(self.nums) > self.pointer
