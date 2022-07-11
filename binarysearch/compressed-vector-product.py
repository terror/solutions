class Solution:
  def solve(self, a, b):
    i = 0; j = 0; ans = 0
    while i < len(a) and j < len(b):
      k = min(a[i], b[j])
      ans += k * a[i + 1] * b[j + 1]
      a[i] -= k; b[j] -= k
      if a[i] == 0:
        i += 2
      if b[j] == 0:
        j += 2
    return ans
