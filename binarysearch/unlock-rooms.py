class Solution:
  def solve(self, rooms):
    adj, vis = defaultdict(set), defaultdict(int)

    for i, r in enumerate(rooms):
      if not r:
        adj[i] = {}
      else:
        for v in r:
          adj[i].add(v)

    def dfs(v):
      vis[v] = 1
      for u in adj[v]:
        if not vis[u]:
          dfs(u)

    dfs(0)

    for i in range(len(rooms)):
      if not vis[i]:
        return False

    return True
