class Solution:
  def solve(self, prices):
    ans = 0
    for i in range(1, len(prices)):
      ans += max(0, prices[i] - prices[i - 1])
    return ans
