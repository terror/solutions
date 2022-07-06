class Solution:
  def solve(self, nums):
    nums = list(filter(lambda x: x > 0, nums))

    if not nums:
      return 1

    d = defaultdict(bool)
    for i in range(len(nums)):
      d[nums[i]] = True

    for i in range(1, len(nums) + 2):
      if not d[i]:
        return i
