class Solution:
  def solve(self, moves):
    a = b = c = 0
    for move in moves:
      a += move == 'L'
      b += move == 'R'
      c += move == '?'
    return max(abs(0 - a + b + c), abs(0 - a + b - c))
