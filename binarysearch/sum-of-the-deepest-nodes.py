# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    if not root:
      return 0

    q, l = [root], 0
    while q:
      ext = []
      while q:
        top = q.pop(0)
        if top.left:
          ext.append(top.left)
        if top.right:
          ext.append(top.right)
      l += 1
      q += ext

    ans = 0
    q = [root]; u = 0
    while q:
      ext = []
      while q:
        top = q.pop(0)
        if u + 1 == l:
          ans += top.val
        if top.left:
          ext.append(top.left)
        if top.right:
          ext.append(top.right)
      q += ext
      u += 1

    return ans
