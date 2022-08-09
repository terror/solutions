class Solution:
  def solve(self, nums):
    nums = sorted(list(set(nums)))
    i = ans = 0
    while i < len(nums):
      j = i + 1
      while j < len(nums) and abs(nums[j - 1] - nums[j]) == 1:
        j += 1
      ans = max(ans, j - i)
      i = j
    return ans
