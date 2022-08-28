MOD = 10 ** 9 + 7

class Solution:
  def solve(self, n, faces, total):
    dp = [[0] * (total + 1) for i in range(n + 1)]

    for i in range(1, min(faces + 1, total + 1)):
      dp[1][i] = 1

    for i in range(2, n + 1):
      for j in range(1, total + 1):
        for k in range(1, min(faces + 1, j)):
          dp[i][j] += dp[i - 1][j - k]

    return dp[-1][-1] % MOD
