# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    if not root:
      return []
    ans = []
    def go(root):
      nonlocal ans
      if root.left:
        go(root.left)
      ans.append(root.val)
      if root.right:
        go(root.right)
    go(root)
    return ans

