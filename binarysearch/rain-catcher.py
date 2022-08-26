class Solution:
  def solve(self, nums):
    if not nums:
      return 0

    l, r = [0] * len(nums), [0] * len(nums)

    l[0] = nums[0]
    for i in range(1, len(nums)):
      l[i] = max(l[i - 1], nums[i])

    r[len(nums) - 1] = nums[len(nums) - 1]
    for i in range(len(nums) - 2, -1, -1):
      r[i] = max(r[i + 1], nums[i])

    ans = 0

    for i in range(len(nums)):
      ans += min(l[i], r[i]) - nums[i]

    return ans
