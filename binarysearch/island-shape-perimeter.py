class Solution:
  def solve(self, m):
    r, c = len(m), len(m[0])
    def bfs(i, j):
      if i < 0 or i >= r:
        return 0

      if j < 0 or j >= c:
        return 0

      if m[i][j] in [0, 'X']:
        return 0

      m[i][j] = 'X'

      return (
        ((i - 1 < 0 or m[i - 1][j] == 0) + (i + 1 == r or m[i + 1][j] == 0) + (j - 1 < 0 or m[i][j - 1] == 0) + (j + 1 == c or m[i][j + 1] == 0)) + bfs(i - 1, j) + bfs(i + 1, j) + bfs(i, j - 1) + bfs(i, j + 1)
      )

    ans = 0

    for i in range(r):
      for j in range(c):
        if m[i][j]:
          ans += bfs(i, j)

    return ans
