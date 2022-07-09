class Solution:
  def solve(self, nums, k):
    ans = [0] * len(nums)
    for i, v in enumerate(nums):
      ans[(i - k) % len(nums)] = v
    return ans
