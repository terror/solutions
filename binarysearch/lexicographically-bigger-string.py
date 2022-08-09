class Solution:
  def solve(self, s, t):
    if len(s) != len(t):
      return False

    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    count = 0

    for a, b in zip(s, t):
      if a > b:
        count += 1
        break

    for a, b in zip(s, t):
      if b > a:
        count += 1
        break

    return count < 2
