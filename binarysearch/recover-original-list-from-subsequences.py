class Solution:
  def solve(self, lists):
    adj, V = defaultdict(set), set()

    for i in range(len(lists)):
      V.update(lists[i])
      for j in range(len(lists[i]) - 1):
        adj[lists[i][j]].add(lists[i][j + 1])

    ans, vis = [], [0] * 1000001

    def dfs(v):
      vis[v] = 1
      for u in adj[v]:
        if not vis[u]:
          dfs(u)
      ans.insert(0, v)

    for u in V:
      if not vis[u]:
        dfs(u)

    return ans
