class Solution:
  def solve(self, n):
    n, ans = str(n), 0
    for i in range(len(n)):
      x = list(n)
      x[i] = '3'
      ans = max(ans, int(''.join(x)))
    return ans
