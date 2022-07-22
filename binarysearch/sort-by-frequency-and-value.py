class Solution:
  def solve(self, nums):
    c = Counter(nums)
    ans = []
    for k, v in sorted(c.items(), key = lambda x: (x[1], x[0]), reverse = True):
        ans += [k] * v
    return ans
