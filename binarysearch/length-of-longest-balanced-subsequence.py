class Solution:
  def solve(self, s):
    a = b = 0
    for ch in s:
      if ch == '(':
        a += 1
      else:
        b += not a
        a -= not not a
    return len(s) - (a + b)
