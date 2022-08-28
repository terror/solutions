class Solution:
  def solve(self, matrix):
    A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    invalid = lambda s: len(set(s)) != len(s) or set(s) != A

    for r in matrix:
      if invalid(r):
        return False

    for c in list(zip(*matrix)):
      if invalid(c):
        return False

    for i in range(0, len(matrix) - 3, 3):
      for j in range(0, len(matrix) - 3, 3):
        if invalid(list(chain(*[row[j:j+3] for row in matrix[i:i+3]]))):
          return False

    return True
