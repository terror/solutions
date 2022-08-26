class Solution:
  def solve(self, n):
    a = b = 1
    while b * (b + 1) < 2 * n:
      x = (1.0 * n - (b * (b + 1)) / 2) / (b + 1)
      a, b = a + int(x - int(x) == 0.0), b + 1
    return a
