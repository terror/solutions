class Solution:
  def solve(self, shows, durations, k):
    d = Counter()

    for a, b in zip(shows, durations):
      d[a] += b

    return sum(map(lambda x: x[1], d.most_common(k)))
