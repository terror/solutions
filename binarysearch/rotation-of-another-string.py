class Solution:
  def solve(self, s0, s1):
    if len(s0) != len(s1):
      return False
    return (s0 in s1 + s1) or (s1 in s0 + s0)
