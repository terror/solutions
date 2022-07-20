class Solution:
  def solve(self, nums):
    ans = 0; c = Counter()
    for n in nums:
      ans += 1 + c[n]
      c[n] += 1
    return ans
