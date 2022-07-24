# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    a, s = Counter(), [(root, 0)]
    while s:
      node, i = s.pop()
      a[i] += node.val
      if node.left:
        s.append((node.left, i + 1))
      if node.right:
        s.append((node.right, i))
    return list(a.values())
