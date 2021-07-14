class Solution:
  def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    l, d = timeSeries, duration
    if len(l) == 0:
      return 0
    ans = 0
    for i in range(len(l) - 1):
      ans += min(l[i + 1] - l[i], d)
    return ans + d
