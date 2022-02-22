class Solution:
  def __init__(self):
    # NWES
    self.dr = [-1, 0, 0, 1]
    self.dc = [0, -1, 1, 0]

  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
      return 0
    n, m, ans = len(grid), len(grid[0]), 0
    for i in range(n):
      for j in range(m):
        if self.floodfill(i, j, '1', 'x', grid, n, m):
          ans += 1
    return ans

  def floodfill(self, r, c, a, b, grid, n, m):
    if r < 0 or r >= n or c < 0 or c >= m:
      return 0
    if grid[r][c] != a:
      return 0
    grid[r][c] = b
    for i in range(4):
      self.floodfill(r + self.dr[i], c + self.dc[i], a, b, grid, n, m)
    return 1
