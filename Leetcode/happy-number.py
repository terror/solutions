class Solution:
  def isHappy(self, n: int) -> bool:
    s = set()
    while True:
      num = n
      Sum = 0
      while num != 0:
        Sum += (num % 10)**2
        num //= 10
      n = Sum
      if Sum in s:
        return False
      else:
        s.add(Sum)
      if Sum == 1:
        break
    return True
