class Solution:
  def solve(self, nums):
    c = sorted(nums)
    r = c[::-1]
    a = b = 0
    for i, v in enumerate(nums):
      if c[i] != v:
        a += abs(v - c[i])
      if r[i] != v:
        b += abs(v - r[i])
    return min(a, b)
