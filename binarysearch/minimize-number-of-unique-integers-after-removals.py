class Solution:
  def solve(self, items, n):
    d = Counter(items)
    for key in sorted(d, key = d.get):
      if d[key] >= n:
        d[key], n = d[key] - n, 0
      else:
        d[key], n = d[key] - n, n - d[key]
    return len([c for c in d if d[c] > 0]
