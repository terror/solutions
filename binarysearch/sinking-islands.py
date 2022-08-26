class Solution:
  def solve(self, board):
    r, c = len(board), len(board[0])

    def dfs(i, j):
      if i < 0 or i >= r or j < 0 or j >= c:
        return ([], False)

      if not board[i][j]:
        return ([], False)

      board[i][j] = 0

      n = dfs(i + 1, j)
      s = dfs(i - 1, j)
      e = dfs(i, j + 1)
      w = dfs(i, j - 1)

      return (
        (
          [(i, j)] + n[0] + s[0] + e[0] + w[0],
          (i - 1 < 0 or i + 1 > r - 1 or j - 1 < 0 or j + 1 > c - 1) | n[1] | s[1] | e[1] | w[1]
        )
      )

    sinks = []

    for i in range(r):
      for j in range(c):
        if board[i][j]:
          result = dfs(i, j)
          sinks.append((result[0], not result[1]))

    for indicies, sink in sinks:
      for i, j in indicies:
        board[i][j] = int(not sink)

    return board
