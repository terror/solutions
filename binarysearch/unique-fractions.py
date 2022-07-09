class Solution:
  def solve(self, fractions):
    def r(a, b):
      if a == 0:
        return (0, 1)
      g = math.gcd(a, b)
      return (a // g, b // g)

    ans = set()
    for a,b  in fractions:
      x, y = r(a, b)
      if (x, y, x // y) in ans:
        continue
      ans.add((x, y, x / y))

    return list(map(lambda x: x[:2], sorted(list(ans), key = lambda x: x[2])))
