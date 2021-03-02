class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        can = len(candyType) // 2
        if len(set(candyType)) >= can:
            return can
        return len(set(candyType))
