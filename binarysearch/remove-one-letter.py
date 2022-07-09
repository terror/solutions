class Solution:
  def solve(self, s0, s1):
    if s0 == s1:
      return False

    if len(s0) - 1 != len(s1):
      return False

    j = 0
    for i in range(len(s0)):
      j += j < len(s1) and s0[i] == s1[j]

    return j == len(s1)
