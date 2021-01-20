class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, i, j = set(), 0, len(height)-1

        while i < j:
            if height[i] < height[j]:
                ans.add(height[i]*(j-i))
                i += 1
            else:
                ans.add(height[j]*(j-i))
                j -= 1
        return max(ans)
