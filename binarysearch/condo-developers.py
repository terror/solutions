class Solution:
  def solve(self, m):
    r = list(map(max, m))
    c = list(map(max, list(zip(*m))))

    for i in range(len(m)):
      for j in range(len(m[0])):
        m[i][j] = min(c[j], r[i])

    return m
