class Solution:
  def solve(self, nums):
    ranks = {}
    for i, rank in enumerate(sorted(list(set(nums)), reverse = True)):
      ranks[rank] = i
    return [ranks[num] for num in nums]
