class Solution:
  def maxCoins(self, piles: List[int]) -> int:
    piles.sort()
    n = len(piles)
    i, j = 0, n - 1
    ans = 0
    while i < j:
      c = piles[j - 1]
      j -= 2
      i += 1
      ans += c
    return ans
