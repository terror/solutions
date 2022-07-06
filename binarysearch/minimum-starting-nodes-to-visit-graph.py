class Solution:
  def solve(self, edges):
    deg = Counter()

    for u, v in edges:
      deg[u] += 0
      deg[v] += 1

    ans = []
    for k in deg:
      if not deg[k]:
        ans.append(k)

    return ans
