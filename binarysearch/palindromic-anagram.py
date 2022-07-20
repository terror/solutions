class Solution:
  def solve(self, s):
    c = Counter(s)
    f = 0
    for k in c:
      f += c[k] & 1
    return f < 2
