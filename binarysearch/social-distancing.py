class Solution:
  def solve(self, s, k):
    previous = -k
    for i in range(len(s)):
      if s[i] == 'x': previous = i
      elif s[i] == '.':
        r = s.find('x', i, len(s))
        if i - previous >= k and (r == -1 or r - i >= k):
          return True
    return False
