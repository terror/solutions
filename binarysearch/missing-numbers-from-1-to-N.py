class Solution:
  def solve(self, nums):
    a = set(nums)
    b = set(i for i in range(1, len(nums) + 1))
    return sorted(list(b.difference(a)))
