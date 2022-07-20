# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    if not root:
      return True
    s = set()
    def dfs(root):
      nonlocal s
      if root.left:
        dfs(root.left)
      s.add(root.val)
      if root.right:
        dfs(root.right)
    dfs(root)
    return len(s) == 1
