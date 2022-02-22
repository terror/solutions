# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def __init__(self):
    self.ans = 0

  def sumOfLeftLeaves(self, root: TreeNode) -> int:
    if not root:
      return 0

    def go(root):
      if root.left:
        if not root.left.right and not root.left.left:
          self.ans += root.left.val
        else:
          go(root.left)
      if root.right:
        go(root.right)

    go(root)
    return self.ans
