class Solution:
  def solve(self, ratings):
    n = len(ratings)

    if not n:
      return 0

    l, r = [1] * n, [1] * n

    for i in range(1, n):
      if ratings[i] > ratings[i - 1]:
        l[i] = l[i - 1] + 1

    for i in range(n - 1, 0, -1):
      if ratings[i] < ratings[i - 1]:
        r[i - 1] = r[i] + 1

    return sum([max(a, b) for (a, b) in zip(l, r)])
