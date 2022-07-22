class Solution:
  def solve(self, s, k):
    r = ['' for _ in range(k)]
    for i in range(len(s)):
      r[i % k] += s[i]
    return r
