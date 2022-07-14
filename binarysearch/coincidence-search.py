class Solution:
  def solve(self, nums):
    def b(t):
      l, r = 0, len(nums) - 1
      while l <= r:
        m = (l + r) // 2
        if nums[m] == t:
          return True
        if nums[m] < t:
          l = m + 1
        else:
          r = m - 1
      return False
    return sum(map(lambda x: b(x), nums))
