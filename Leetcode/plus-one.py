class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    carry = 1
    for i in range(len(digits))[::-1]:
      if digits[i] + carry > 9:
        if i == 0:
          digits[i] = 1
          digits.append(0)
          break
        digits[i] = 0
        carry = 1
      else:
        digits[i] += carry
        carry = 0
    return digits
