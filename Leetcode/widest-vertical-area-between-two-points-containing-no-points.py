class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        mx = 0
        for i in range(1, len(points)):
            x, y = points[i]
            a, b = points[i-1]
            mx = max(mx, x-a)
        return mx
