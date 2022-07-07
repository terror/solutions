class Solution:
  def solve(self, board, word):
    for row in board:
      if word in ''.join(row):
        return True

    for i in range(len(board[0])):
      s = board[0][i]
      for j in range(len(board)):
        s += board[j][i]
      if word in s:
        return True

    return False
