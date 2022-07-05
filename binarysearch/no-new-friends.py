MXN = int(2e5)

class Solution:
  def solve(self, n, friends):
    deg = Counter()

    for (u, v) in friends:
      deg[u] += 1
      deg[v] += 1

    for v in range(n):
      if not deg[v]:
        return False

    return True
