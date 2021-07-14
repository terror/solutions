class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """
    # I
    i = len(nums) - 1
    while i > 0:
      if nums[i] > nums[i - 1]:
        break
      i -= 1

    # II
    if i == 0:
      nums.sort()
      return

    # III
    j, k = i + 1, i
    while j < len(nums):
      if nums[j] > nums[i - 1] and nums[j] < nums[k]:
        k = j
      j += 1

    # IV
    nums[i - 1], nums[k] = nums[k], nums[i - 1]

    # V (this uses extra memory, use quicksort for no extra memory)
    nums[i:len(nums)] = sorted(nums[i:len(nums)])
