# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    foo = []
    def go(root):
      nonlocal foo
      if root.left:
        go(root.left)
      foo.append(root.val)
      if root.right:
        go(root.right)
    go(root)
    return foo == foo[::-1]
