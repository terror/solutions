class Solution:
  def solve(self, nums):
    return (lambda d: [key for key in sorted(d) if d[key] > len(nums) // 3])(Counter(nums))
