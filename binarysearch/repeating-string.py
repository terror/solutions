class Solution:
  def solve(self, s):
    for i in range(len(s)):
      sub = s[0:i]
      if len(sub) == 0:
        continue
      if len(s) % len(sub) == 0 and sub * (len(s) // len(sub)) == s:
        return True
    return False
