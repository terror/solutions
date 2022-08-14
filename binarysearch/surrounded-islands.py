class Solution:
  def solve(self, m):
    r, c = len(m), len(m[0])

    def fill(i, j):
      if i < 0 or i >= r or j < 0 or j >= c:
        return 0

      if not m[i][j]:
        return 0

      m[i][j] = 0

      return (i == 0 or j == 0 or i == r - 1 or j == c - 1) | fill(i - 1, j) | fill(i + 1, j) | fill(i, j - 1) | fill(i, j + 1)

    ans = 0

    for i in range(r):
      for j in range(c):
        if m[i][j]:
          ans += not fill(i, j)

    return ans
