class Solution:
  def solve(self, piles):
    piles.sort(reverse = True)
    return sum([piles[i + 1] for i in range(0, len(piles) - len(piles) // 3, 2)])
