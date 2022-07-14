class Solution:
  def solve(self, times):
    if not times:
      return 0

    times.sort(key = lambda x: x[1])

    ans, prev_end = 1, times[0][1]

    for start, end in times[1:]:
      if start > prev_end:
        ans += 1
        prev_end = end

    return ans
