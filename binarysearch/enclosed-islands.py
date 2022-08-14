class Solution:
  def solve(self, m):
    r, c = len(m), len(m[0])

    def fill(i, j):
      if i < 0 or j < 0 or j >= c or i >= r:
        return (0, 0)

      if not m[i][j]:
        return (0, 0)

      m[i][j] = 0

      n = fill(i + 1, j)
      s = fill(i - 1, j)
      e = fill(i, j + 1)
      w = fill(i, j - 1)

      return (
        1 + n[0] + s[0] + e[0] + w[0],
        (i == 0 or j == 0 or j == c - 1 or i == r - 1) | n[1] | s[1] | e[1] | w[1]
      )

    ans = 0

    for i in range(r):
      for j in range(c):
        if m[i][j]:
          result = fill(i, j)
          ans += result[0] * (not result[1])

    return ans
