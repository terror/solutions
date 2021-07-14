class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    f = flowerbed
    ans = 0
    for i in range(len(f)):
      if f[i] == 0:
        l, r = max(0, i - 1), min(i + 1, len(f) - 1)
        if f[r] == 0 and f[l] == 0:
          f[i] = 1
          ans += 1
    return ans >= n
