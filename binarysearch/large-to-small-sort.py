class Solution:
  def solve(self, nums):
    ans = []; nums.sort()
    i = 0; j = len(nums) - 1
    while i < j:
      ans.append(nums[j])
      ans.append(nums[i])
      i += 1
      j -= 1
    if len(nums) & 1: ans.append(nums[i])
    return ans
