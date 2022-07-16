class Solution:
  def solve(self, s, t):
    if s == t:
      return True
    for v in Counter(s + t).values():
      if v % 2 != 0:
        return False
    return True
