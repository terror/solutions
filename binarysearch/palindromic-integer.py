class Solution:
  def solve(self, num):
    rev = 0; x = num
    while x > 0:
      rev = (rev * 10) + (x % 10)
      x //= 10
    return rev == num
