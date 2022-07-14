class Solution:
  def solve(self, nums):
    d = defaultdict(bool)

    for n in nums:
      d[n] = True

    ans = 0

    for n in nums:
      if d[n + 1]:
        ans += 1

    return ans
