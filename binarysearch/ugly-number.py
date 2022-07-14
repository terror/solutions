class Solution:
  def solve(self, n):
    if n == 0: return False

    i, f = 2, []

    while i * i <= n:
      if n % i: i += 1
      else:
        n //= i
        f.append(i)

    if n > 1:
      f.append(n)

    return all(x in [2, 3, 5] for x in f)
