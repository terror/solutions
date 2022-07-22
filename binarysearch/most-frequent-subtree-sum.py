# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    d = Counter()
    def go(root):
      if not root:
        return 0
      s = root.val + go(root.left) + go(root.right)
      d[s] += 1
      return s
    go(root)
    return d.most_common()[0][0]
