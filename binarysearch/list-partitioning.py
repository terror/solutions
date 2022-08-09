class Solution:
  def solve(self, strs):
    c, ans = Counter(strs), []
    for key in ["red", "green", "blue"]:
      ans += [key] * c[key]
    return ans
