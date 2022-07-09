class Solution:
  def solve(self, nums):
    c = Counter(); ans = 0
    for n in nums:
      ans += c[n]
      c[n] += 1
    return ans
