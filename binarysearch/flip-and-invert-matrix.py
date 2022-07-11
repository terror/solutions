class Solution:
  def solve(self, matrix):
    return list(map(lambda x: list(map(lambda x: x ^ 1, reversed(x))), matrix))
