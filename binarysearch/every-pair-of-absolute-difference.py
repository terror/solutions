class Solution:
  def solve(self, nums):
    ans, MOD = 0, 10**9 + 7
    for i in range(len(nums) - 1, -1, -1):
      ans += (i * nums[i] - (len(nums) - 1 - i) * nums[i]) * 2
    return ans % MOD
