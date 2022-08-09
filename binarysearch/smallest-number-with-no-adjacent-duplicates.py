class Solution:
  def solve(self, s):
    s = list(s)
    for i, v in enumerate(s):
      if v == '?':
        adj = []
        if i - 1 >= 0:
          adj.append(s[i - 1])
        if i + 1 < len(s):
          adj.append(s[i + 1])
        s[i] = '1' * ('1' not in adj) or '2' * ('2' not in adj) or '3'
    return ''.join(s)
