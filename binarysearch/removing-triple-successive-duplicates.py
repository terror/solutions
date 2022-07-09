class Solution:
  def solve(self, s):
    i = 0; ans = 0
    while i < len(s) - 1:
      j = i + 1
      while j < len(s) and s[j] == s[i]:
        j += 1
      ans += (j - i) // 3
      i = j
    return ans
