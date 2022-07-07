class Solution:
  def solve(self, nums):
    curr = defaultdict(bool)
    for num in nums:
      if curr[num]:
        return True
      curr[num * 3] = True
      curr[num / 3] = True
    return False
