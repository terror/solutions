class Solution:
  def solve(self, adj):
    dp, vis = [0] * (len(adj) + 1), defaultdict(bool)

    def dfs(v):
      vis[v] = 1
      for u in adj[v]:
        if not vis[u]:
          dfs(u)
        dp[v] = max(dp[v], 1 + dp[u])

    for v in range(len(adj)):
      if not vis[v]:
        dfs(v)

    return max(dp)
