class Solution:
  def solve(self, s):
    i = 0; ans = ''
    while i < len(s):
      ans += s[i]
      j = i + 1
      while j < len(s) and s[j] == s[i]:
        j += 1
      i = j
    return ans
