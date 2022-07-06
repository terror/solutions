class Solution:
  def solve(self, text, word0, word1):
    if not word0 in text or not word1 in text:
      return -1
    a = b = None; c = float('inf')
    for i, v in enumerate(text.split()):
      if v == word0:
        a = i
      if v == word1:
        b = i
      if a is not None and b is not None:
        print(a, b)
        c = min(c, abs(abs(a - b) - 1))
    return c
