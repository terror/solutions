class Solution:
  def solve(self, edges):
    d = defaultdict(set)

    for u, v in edges:
      d[u].add(v)
      d[v].add(u)

    vis = defaultdict(bool)

    def cycle(v, par = -1):
      vis[v] = 1
      for u in d[v]:
        if u == par: continue
        if vis[u] or cycle(u, v): return True
      return False

    for v in range(len(d)):
      if not vis[v] and cycle(v):
        return False

    return True
