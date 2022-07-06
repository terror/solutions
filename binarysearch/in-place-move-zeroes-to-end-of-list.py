class Solution:
  def solve(self, nums):
    l = 0
    for i, v in enumerate(nums):
      if v != 0:
        nums[l], nums[i] = nums[i], nums[l]
        l += 1
    return nums

