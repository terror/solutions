class Solution:
  def solve(self, relations):
    d = defaultdict(list)
    ans = []
    for (a, b) in relations:
      d[a].append(b)
      if b in d[a] and a in d[b]:
        ans += [a, b]
    return sorted(set(ans))
