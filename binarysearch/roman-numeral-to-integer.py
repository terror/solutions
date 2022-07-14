class Solution:
  def solve(self, numeral):
    d = {
      'I':  1,
      'IV': 4,
      'V':  5,
      'IX': 9,
      'X':  10,
      'XL': 40,
      'L':  50,
      'XC': 90,
      'C':  100,
      'CD': 400,
      'D':  500,
      'CM': 900,
      'M':  1000
    }

    i = ans = 0
    while i < len(numeral):
      j = i + 1
      if numeral[i:j+1] in d:
        ans += d[numeral[i:j+1]]
        i = j + 1
      else:
        ans += d[numeral[i]]
        i += 1

    return ans
