class Solution:
  def solve(self, nums, k):
    h = []

    for num in nums:
      heappush(h, -num)

    while k:
      heappush(h, heappop(h) + 1)
      k -= 1

    return -heappop(h)
