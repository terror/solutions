class Solution:
  def solve(self, nums):
    msf = nums[0]; ans = nums[0]
    for i in range(1, len(nums)):
      msf = max(nums[i], msf + nums[i])
      ans = max(ans, msf)
    return ans
