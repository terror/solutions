class Solution:
  def solve(self, nums):
    if not nums:
      return False

    if sum(nums) < 0:
      return True

    a = b = nums[0]
    for i in range(1, len(nums)):
      a = max(nums[i], a + nums[i])
      b = max(a, b)

    return b > sum(nums)
