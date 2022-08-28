class Solution:
  def solve(self, nums):
    nums.sort()
    return nums[-1] > nums[-2] * 2
