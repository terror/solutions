# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    ans = 0
    def dfs(node):
      nonlocal ans
      if not node: return 0
      l, r = dfs(node.left), dfs(node.right)
      ans = max(ans, 1 + l + r)
      return 1 + max(l, r)
    dfs(root)
    return ans
