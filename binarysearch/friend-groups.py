class Solution:
  def solve(self, friends):
    d = defaultdict(set)

    for i, f in enumerate(friends):
      if not f:
        d[i] = {}
      else:
        for v in f:
          d[i].add(v)
          d[v].add(i)

    vis = defaultdict(int)

    def dfs(v):
      vis[v] = 1
      for u in d[v]:
        if not vis[u]:
          dfs(u)

    ans = 0

    def cc(v):
      nonlocal ans
      for i in range(v):
        if not vis[i]:
          ans += 1
          dfs(i)

    cc(len(friends))

    return ans
