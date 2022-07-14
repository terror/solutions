class Solution:
  def solve(self, nums, k):
    s = sum(nums)
    for n in nums:
      if (s - n) / (len(nums) - 1) == k:
        return True
    return False
