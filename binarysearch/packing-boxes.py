class Solution:
  def solve(self, nums):
    if not nums:
      return []

    ret = []

    j = k = 0
    for i in range(1, len(nums)):
      if nums[i] != nums[i - 1]:
        ret.append(nums[j:k+1])
        j = i
      k += 1

    ret.append(nums[j:])

    return ret
