class RangeSum:
    def __init__(self, nums):
      def pre(L):
        ret = [L[0]]
        for i in range(1, len(L)):
          ret.append(ret[i - 1] + L[i])
        return ret
      self.prefix = pre(nums)

    def total(self, i, j):
      if j == 0:
        return 0
      if i == 0:
        return self.prefix[j - 1]
      return self.prefix[j - 1] - self.prefix[i - 1]
