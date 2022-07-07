class Solution:
  def solve(self, m):
    u = m[0]

    if len(set(u)) != len(u):
      return False

    u = set(u)

    for r in m:
      if u != set(r):
        return False

    m = list(zip(*m))

    for c in m:
      if u != set(c):
        return False

    return True
