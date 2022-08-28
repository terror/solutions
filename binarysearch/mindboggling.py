class Solution:
  def solve(self, matrix, words):
    R = C = 4

    vis = defaultdict(bool)

    def dfs(i, j, word, idx):
      if idx == len(word):
        return True

      if i < 0 or i >= R or j < 0 or j >= C:
        return False

      if matrix[i][j] != word[idx] or vis[(i, j)]:
        return False

      vis[(i, j)] = True

      for r, c in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        if dfs(i + r, j + c, word, idx + 1):
          return True

    ans = 0

    for word in words:
      found = 0
      for i in range(R):
        if found:
          break
        for j in range(C):
          if found:
            break
          if matrix[i][j] == word[0] and dfs(i, j, word, 0):
            ans, found = ans + 1, 1
          vis.clear()

    return ans
