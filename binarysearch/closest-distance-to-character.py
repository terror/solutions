class Solution:
  def solve(self, s, c):
    ret = []
    for i, v in enumerate(s):
      if v == c:
        ret.append(0)
      else:
        a, b = s.find(c, i), s.rfind(c, 0, i)
        if b == -1:
          ret.append(abs(i - a))
        else:
          ret.append(min(abs(i - a), abs(i - b)))
    return ret
