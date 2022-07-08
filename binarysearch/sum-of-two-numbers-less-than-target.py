class Solution:
  def solve(self, nums, target):
    nums.sort()
    i = 0; j = len(nums) - 1; ans = float('-inf')
    while i < j:
      s = nums[i] + nums[j]
      if s < target:
        ans = max(ans, s)
      if s >= target:
        j -= 1
      else:
        i += 1
    return ans
