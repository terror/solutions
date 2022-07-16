class Solution:
  def solve(self, nums, k):
    intervals, total = [], 0

    for i in range(1, len(nums)):
      if abs(nums[i] - nums[i - 1]) > 1:
        interval = (nums[i - 1] + 1, nums[i] - 1)
        total += interval[1] - interval[0]
        intervals.append(interval)

    if total <= k:
      intervals.append((nums[-1] + 1, nums[-1] + (k + 1 - total)))

    curr = 0
    for start, end in intervals:
      if curr + (end + 1 - start) > k:
        return start + (k - curr)
      curr += end + 1 - start
