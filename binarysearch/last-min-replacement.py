class Solution:
  def solve(self, nums):
    m = float('inf')
    for i, v in enumerate(nums):
      m = min(m, v)
      nums[i] = m
    return [0] + nums[:-1]
