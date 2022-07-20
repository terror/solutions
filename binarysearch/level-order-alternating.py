# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    i = 0
    q = [root]
    ans = []
    while q:
      ext = []; curr = []
      while q:
        top = q.pop(0)
        curr.append(top.val)
        if top.left:
          ext.append(top.left)
        if top.right:
          ext.append(top.right)
      ans += (curr, curr[::-1])[i != 0]
      q += ext
      i ^= 1
    return ans
