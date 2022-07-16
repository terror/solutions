class Solution:
  def solve(self, s):
    f, v = False, list(Counter(s).values())
    for u in v:
      if u % 3 == 0:
        continue
      if f:
        return False
      if u - 2 < 0 or (u - 2) % 3 != 0:
        return False
      f = True
    return f
