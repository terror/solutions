class Solution:
  def solve(self, nums, k):
    h = []

    for n in nums:
      heappush(h, n)

    while k:
      heappop(h)
      k -= 1

    return heappop(h)
