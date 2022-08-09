class Solution:
  def solve(self, s):
    a, b = [0] * len(s), [0] * len(s)

    seen = set()
    for i in range(len(s)):
      seen.add(s[i])
      a[i] = len(seen)

    seen = set()
    for i in range(len(s) - 1, -1, -1):
      seen.add(s[i])
      b[i] = len(seen)

    ans = 0

    for i in range(len(s) - 1):
      if a[i] == b[i + 1]:
        ans += 1

    return ans
