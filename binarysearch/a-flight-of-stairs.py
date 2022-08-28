MOD = 10 ** 9 + 7

class Solution:
  def solve(self, n):
    dp = [0] * (n + 2)
    dp[1] = 1
    for i in range(2, n + 2):
      dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n + 1] % MOD
