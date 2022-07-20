class Solution:
  def solve(self, words):
    d = Counter()
    for w in words:
      counts = [0] * 26
      for c in w:
        counts[ord(c) - ord('a')] += 1
      d[tuple(counts)] += 1
    return d.most_common()[0][1]
