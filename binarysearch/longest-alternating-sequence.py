class Solution:
  def solve(self, nums):
    if not nums: return 0
    a = b = 1
    for i in range(1, len(nums)):
      if nums[i] - nums[i - 1] > 0:
        a = b + 1
      elif nums[i] - nums[i - 1] < 0:
        b = a + 1
    return max(a, b)
