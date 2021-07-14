# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def __init__(self):
    self.d = set()
    self.ans = 0

  def findTarget(self, root: TreeNode, k: int) -> bool:
    def go(root, k):
      if root.right:
        go(root.right, k)
      if root.left:
        go(root.left, k)
      if root.val in self.d:
        self.ans = 1
      self.d.add(k - root.val)

    go(root, k)
    return self.ans
