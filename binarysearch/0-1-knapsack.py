class Solution:
  def solve(self, weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(1, len(weights) + 1):
      for j in range(capacity, 0, -1):
        if weights[i - 1] <= j:
          dp[j] = max(dp[j], dp[j - weights[i - 1]] + values[i - 1])
    return dp[capacity
