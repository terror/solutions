# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root, lo, hi):
    if not root:
      return 0
    q, a = [root], 0
    while q:
      top = q.pop(0)
      a += lo <= top.val <= hi
      if top.left:
        q.append(top.left)
      if top.right:
        q.append(top.right)
    return a
