class Solution:
  def solve(self, s1, s2):
    if s1 == s2:
      return True

    j = 0
    for i in range(len(s2)):
      j += j < len(s1) and s2[i] == s1[j]

    return j == len(s1)
