class Solution:
  def solve(self, nums):
    if not nums:
      return 0

    a = b = c = d = nums[0]
    for i in range(1, len(nums)):
      a = max(nums[i], nums[i] + a)
      b = max(a, b)
      c = min(nums[i], nums[i] + c)
      d = min(c, d)

    return max(b, abs(d))
