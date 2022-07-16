# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    if not root:
      return [0, 0]

    a = b = 0

    def go(root):
      nonlocal a, b
      if root.left:
        go(root.left)
      if not root.left and not root.right:
        a += 1
      else: b += 1
      if root.right:
        go(root.right)

    go(root)

    return [a, b]
