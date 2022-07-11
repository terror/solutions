# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    if not root:
      return 0
    q, ans = [(root, False)], 0
    while q:
      top, x = q.pop(0)
      if x and not top.right and not top.left:
        ans += top.val
      if top.right:
        q.append((top.right, True))
      if top.left:
        q.append((top.left, False))
    return ans
