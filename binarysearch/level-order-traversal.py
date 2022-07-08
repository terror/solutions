# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    q, ans = [root], []
    while q:
      top = q.pop(0)
      ans.append(top.val)
      if top.left:
       q.append(top.left)
      if top.right:
        q.append(top.right)
    return ans
