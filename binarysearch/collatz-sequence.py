class Solution:
  def solve(self, n):
    ans = 1
    while n != 1:
      ans += 1
      n = (n // 2, 3 * n + 1)[n % 2 != 0]
    return ans
