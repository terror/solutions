class Solution:
  def solve(self, matrix):
    if not matrix:
      return 0

    def fill(r, c, a, b):
      nonlocal matrix

      if r < 0 or r >= len(matrix):
        return 0

      if c < 0 or c >= len(matrix[0]):
        return 0

      if matrix[r][c] != a:
        return 0

      matrix[r][c] = b

      dr = [-1, 0, 0, 1]
      dc = [0, -1, 1, 0]

      for i in range(4):
        fill(r + dr[i], c + dc[i], a, b)

      return 1

    ans = 0
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        ans += fill(i, j, 1, -1)

    return ans
