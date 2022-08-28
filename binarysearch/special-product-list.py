class Solution:
  def solve(self, nums):
    l, r, n = 1, 1, len(nums)

    ans = [1] * n

    for i in range(n):
      if i - 1 >= 0:
        l *= nums[i - 1]
        ans[i] = l

    for j in range(n - 1, -1, -1):
      if j + 1 <= n - 1:
        r *= nums[j + 1]
        ans[j] *= r

    return ans
