class Solution:
  def solve(self, num):
    ans = 0
    while num:
      ans += num % 10
      num //= 10
    return ans
