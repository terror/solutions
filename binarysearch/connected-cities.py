MXN = int(2e5)

class Graph:
  def __init__(self):
    self.adj = defaultdict(list)
    self.rev = defaultdict(list)
    self.vis = [0] * MXN
    self.s = []

  def add(self, u, v):
    self.adj[u].append(v)
    self.rev[v].append(u)

  def order(self, v):
    self.vis[v] = 1
    for u in self.adj[v]:
      if not self.vis[u]:
        self.order(u)
    self.s.append(v)

  def dfs(self, v):
    self.vis[v] = 1
    for u in self.rev[v]:
      if not self.vis[u]:
        self.dfs(u)

  def run(self):
    ans = 0
    while self.s:
      v = self.s.pop()
      if not self.vis[v]:
        self.dfs(v)
        ans += 1
    return ans

class Solution:
  def solve(self, n, roads):
    g = Graph()

    for (u, v) in roads:
      g.add(u, v)

    for v in range(n):
      if not g.vis[v]:
        g.order(v)

    for v in range(n):
      g.vis[v] = 0

    return g.run() == 1
