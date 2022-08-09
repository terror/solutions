class Solution:
  def solve(self, orders):
    d = Counter()
    seen = set()
    for order in orders:
      if order in seen:
        return False
      d[order[1]] += (1, -1)[order[0] == 'D']
      if d[order[1]] < 0:
        return False
      seen.add(order)
    return all(c == 0 for c in d.values())
