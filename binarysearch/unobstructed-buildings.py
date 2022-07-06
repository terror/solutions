class Solution:
  def solve(self, heights):
    curr = 0; ans = []
    for i, height in enumerate(heights[::-1]):
      if height > curr:
        curr = height
        ans.append(len(heights) - i - 1)
    return sorted(ans)
