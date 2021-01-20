# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        d = collections.Counter()

        def go(root):
            if root.left:
                go(root.left)
            if root.right:
                go(root.right)
            d[root.val] += 1
        go(root)
        w = max(d.values())
        ans = []
        for i in d:
            if d[i] == w:
                ans.append(i)
        return ans
