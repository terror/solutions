# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, tree, target):
    q = [tree]
    while q:
      ext = []; curr = []
      while q:
        top = q.pop(0)
        curr.append(top)
        if top.left:
          ext.append(top.left)
        if top.right:
          ext.append(top.right)
      for i in range(len(curr)):
        if curr[i].val == target:
          if i + 1 == len(curr):
            return None
          return curr[i + 1]
      q += ext
