class Solution:
  def solve(self, lst, p):
    ans = [0] * len(lst)
    for i, v in enumerate(lst):
      ans[p[i]] = v
    return ans
