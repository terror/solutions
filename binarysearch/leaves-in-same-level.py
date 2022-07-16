# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    if not root:
      return False
    q = [root]; level = 0; s = set()
    while q:
      ext = []
      while q:
        top = q.pop(0)
        if not top.left and not top.right:
          s.add(level)
        if top.left:
          ext.append(top.left)
        if top.right:
          ext.append(top.right)
      q += ext
      level += 1
    return len(s) == 1
