class Solution:
  def solve(self, lists):
    h = []

    for l in lists:
      for e in l:
        heappush(h, e)

    ans = []

    while h:
      ans.append(heappop(h))

    return ans
