class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    # dp solution time complexity O(n)
    best = Max = nums[0]

    for i in range(1, len(nums)):
      best = max(nums[i], nums[i] + best)
      if best > Max:
        Max = best

    return Max
