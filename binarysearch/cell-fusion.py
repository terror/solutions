class Solution:
  def solve(self, cells):
    h = []

    for c in cells:
      heappush(h, -c)

    s = []

    while len(h) > 1:
      a = -heappop(h)
      b = -heappop(h)
      if a == b:
        continue
      heappush(h, -floor((a + b) / 3))

    while h:
      s.append(-heappop(h))

    if not s:
      return -1

    return s[-1]
