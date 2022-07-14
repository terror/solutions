class Solution:
  def solve(self, nums):
    c, ans = Counter(nums), int(2e5)
    for k in c:
      if c[k] == max(c.values()):
        ans = min(ans, len(nums) - nums[::-1].index(k) - nums.index(k))
    return ans
