class Solution:
  def solve(self, matrix):
    if not matrix:
      return 0

    r, c = len(matrix), len(matrix[0])

    Q, count = deque(), 0

    for i in range(r):
      for j in range(c):
        count += matrix[i][j] == 1
        if matrix[i][j] == 2:
          Q.append((i, j))

    ans = 0

    while Q:
      for _ in range(len(Q)):
        i, j = Q.popleft()
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
          if 0 <= i + x < r and 0 <= j + y < c and matrix[i + x][j + y] == 1:
            matrix[i + x][j + y] = 2
            count -= 1
            Q.append((i + x, j + y))
      ans += 1

    return max(0, ans - 1) if count == 0 else -1
