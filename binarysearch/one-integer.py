class Solution:
  def solve(self, nums):
    if len(nums) < 2: return 0
    heapify(nums)
    cost = 0
    while len(nums) != 1:
      val = heappop(nums) + heappop(nums)
      cost += val
      heappush(nums, val)
    return cost
