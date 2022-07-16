# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, a, b, target):
    def preprocess(root):
      d = defaultdict(bool)
      if not root:
        return d
      q = [root]
      while q:
        top = q.pop(0)
        d[target - top.val] = True
        if top.left:
          q.append(top.left)
        if top.right:
          q.append(top.right)
      return d

    def go(root, d):
      if not root:
        return False
      q = [root]
      while q:
        top = q.pop(0)
        if top.val in d:
          return True
        if top.left:
          q.append(top.left)
        if top.right:
          q.append(top.right)
      return False

    return go(b, preprocess(a))
