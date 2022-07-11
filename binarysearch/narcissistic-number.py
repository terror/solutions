class Solution:
  def solve(self, n):
    p, t = 0, n
    while t:
      p += 1
      t //= 10

    a, t = 0, n
    while t:
      a += (t % 10) ** p
      t //= 10

    return a == n
