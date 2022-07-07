class Solution:
  def solve(self, graph):
    adj = defaultdict(list)

    for i, v in enumerate(graph):
      for u in v:
        adj[u].append(i)

    return [adj[v] for v in range(len(graph))]
