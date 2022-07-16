class Solution:
  def solve(self, s0, s1):
    if len(s0) != len(s1):
      return False

    c = Counter()

    for i in range(len(s0)):
      c[s0[i]] += 1
      c[s1[i]] -= 1

    for k in c:
      if c[k] != 0:
        return False

    return True
