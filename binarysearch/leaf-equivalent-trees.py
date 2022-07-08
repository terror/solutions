# class Tree:
#   def __init__(self, val, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
class Solution:
  def solve(self, root0, root1):
    def go(root, acc):
      if root.left:
        go(root.left, acc)
      if not root.right and not root.left:
        acc.append(root.val)
      if root.right:
        go(root.right, acc)
      return acc
    return go(root0, []) == go(root1, [])
