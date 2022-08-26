class Solution:
  def solve(self, points, k):
    d = defaultdict(set)

    for i in range(len(points)):
      for j in range(len(points)):
        if dist(points[i], points[j]) <= k:
          d[tuple(points[i])].add(tuple(points[j]))
          d[tuple(points[j])].add(tuple(points[i]))

    vis = defaultdict(bool)

    def dfs(v):
      vis[v] = 1
      for u in d[v]:
        if not vis[u]:
          dfs(u)

    ans = 0

    for p in points:
      if not vis[tuple(p)]:
        dfs(tuple(p))
        ans += 1

    return ans
