# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    if not root:
      return 0
    def dfs(root):
      if not root:
        return -inf
      if not root.left and not root.right:
        return root.val
      l = dfs(root.left)
      r = dfs(root.right)
      return (l, r)[r > l] + root.val
    return dfs(root)
