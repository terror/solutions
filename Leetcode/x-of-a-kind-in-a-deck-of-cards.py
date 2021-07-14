class Solution:
  def hasGroupsSizeX(self, deck: List[int]) -> bool:
    return math.gcd(*list(collections.Counter(deck).values())) >= 2
