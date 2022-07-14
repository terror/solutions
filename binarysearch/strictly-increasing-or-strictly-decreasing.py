class Solution:
  def solve(self, nums):
    dec = inc = True

    for i in range(1, len(nums)):
      if nums[i - 1] <= nums[i]:
        dec = False; break

    for i in range(1, len(nums)):
      if nums[i - 1] >= nums[i]:
        inc = False; break

    return inc or dec
