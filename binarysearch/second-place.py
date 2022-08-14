# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    if not root:
      return 0
    q, level, depths = [root], 0, {}
    while q:
      for _ in range(len(q)):
        top = q.pop(0)
        if not top.left and not top.right:
          depths[level] = True
        if top.left:
          q.append(top.left)
        if top.right:
          q.append(top.right)
      level += 1
    return sorted(depths)[-2]
