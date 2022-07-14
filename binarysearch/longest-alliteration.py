class Solution:
  def solve(self, words):
    ans = 0; i = 0
    while i < len(words):
      j = i + 1
      while j < len(words) and words[i][0] == words[j][0]:
        j += 1
      ans = max(ans, j - i)
      i = j
    return ans
