class Solution:
  def solve(self, matrix):
    if not matrix:
      return 0

    r, c = len(matrix), len(matrix[0])

    dist = [[0] * c for _ in range(r)]

    q = deque((a, b) for a in range(r) for b in range(c) if not matrix[a][b])

    if len(q) in (0, r * c):
      return -1

    while q:
      a, b = q.popleft()

      for x, y in [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]:
        if 0 <= x < r and 0 <= y < c and matrix[x][y]:
          matrix[x][y] = 0
          dist[x][y] = dist[a][b] + 1
          q.append((x, y))

    return max(max(row) for row in dist)
