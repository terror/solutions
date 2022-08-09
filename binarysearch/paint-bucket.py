class Solution:
  def solve(self, matrix, r, c, target):
    n, m = len(matrix), len(matrix[0])

    start = matrix[r][c]

    def fill(i, j):
      if i < 0 or i >= n:
        return

      if j < 0 or j >= m:
        return

      if matrix[i][j] == target or matrix[i][j] != start:
        return

      matrix[i][j] = target

      for r, c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        fill(i + r, j + c)

    fill(r, c)

    return matrix

