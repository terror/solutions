class Solution:
  def solve(self, nums):
    d = defaultdict(bool); mx = -1
    for num in nums:
      d[num] = True
      if d[num] and d[-num]:
        mx = max(mx, abs(num))
    return mx
