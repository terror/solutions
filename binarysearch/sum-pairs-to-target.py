class Solution:
  def solve(self, nums, target):
    nums.sort()
    i = 0; j = len(nums) - 1; ans = 0
    while i < j:
      s = nums[i] + nums[j]
      if s == target:
        ans += 1
        i += 1
        j -= 1
      elif s < target:
        i += 1
      else:
        j -= 1
    return ans
