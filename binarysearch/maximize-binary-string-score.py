class Solution:
  def solve(self, s):
    a = 0; b = s.count('1'); ans = float('-inf')
    for i in range(len(s) - 1):
      if s[i] == '0': a += 1
      else: b -= 1
      ans = max(ans, a + b)
    return ans
