class Solution:
  def solve(self, s):
    ans = 0
    for k, g in groupby(s):
      N = len(list(g))
      ans += (N * (N + 1)) // 2
    return ans
