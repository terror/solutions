class Solution:
  def solve(self, a, b):
    for x, y in zip(a, b):
      if x != y:
        return (x, y)[a[-1] not in b]
