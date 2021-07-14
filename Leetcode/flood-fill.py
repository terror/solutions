class Solution:
  def __init__(self):
    self.n = self.m = self.start = 0

  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    if image[sr][sc] == newColor:
      return image

    self.n = len(image)
    self.m = len(image[0])
    self.start = image[sr][sc]

    self.dfs(sr, sc, image, newColor)
    return image

  def dfs(self, r, c, image, newColor):
    if r >= self.n or r < 0 or c >= self.m or c < 0:
      return 0

    if image[r][c] != self.start:
      return 0

    image[r][c] = newColor

    self.dfs(r - 1, c, image, newColor)
    self.dfs(r + 1, c, image, newColor)
    self.dfs(r, c + 1, image, newColor)
    self.dfs(r, c - 1, image, newColor)
