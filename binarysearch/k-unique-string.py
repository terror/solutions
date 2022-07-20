class Solution:
  def solve(self, s, k):
    ops = len(set(s)) - k

    if ops <= 0:
      return 0

    ans = 0

    for k, v in sorted(Counter(s).items(), key = lambda x: x[1]):
      if ops == 0:
        break
      ans += v
      ops -= 1

    return ans
