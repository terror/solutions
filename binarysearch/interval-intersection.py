class Solution:
  def solve(self, intervals):
    a = 0; b = float('inf')
    for s, e in intervals:
      a = max(a, s)
      b = min(b, e)
    return [a, b]
