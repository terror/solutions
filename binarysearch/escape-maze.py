class Solution:
  def solve(self, matrix):
    r, c = len(matrix), len(matrix[0])

    if r == 0 or c == 0 or matrix[0][0] == 1 or matrix[r - 1][c - 1] == 1:
      return -1

    q, vis = deque(), defaultdict(bool)
    q.append((0, 0, 0))
    vis[(0, 0)] = True

    while q:
      i, j, dist = q.popleft()

      if i == r - 1 and j == c - 1:
        return dist + 1

      for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if i + x >= 0 and i + x < r and j + y >= 0 and j + y < c and not vis[(i + x, j + y)] and matrix[i + x][j + y] != 1:
          q.append((i + x, j + y, dist + 1))
          vis[(i + x, j + y)] = True

    return -1
