# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def go(root):
            if root.left:
                go(root.left)
            if root.right:
                go(root.right)
            self.ans.append(root.val)
        go(root)
        return self.ans
