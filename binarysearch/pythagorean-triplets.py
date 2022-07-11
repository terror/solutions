class Solution:
  def solve(self, nums):
    squares = set()
    for num in nums:
      squares.add(num ** 2)
    for a in nums:
      for b in nums:
        if a ** 2 + b ** 2 in squares:
          return True
    return False
