# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def averageOfLevels(self, root: TreeNode) -> List[float]:
    d, lvl, ans = collections.defaultdict(list), 0, []

    def preorder(root, lvl):
      if root is None:
        return
      d[lvl].append(root.val)
      preorder(root.left, lvl + 1)
      preorder(root.right, lvl + 1)

    preorder(root, lvl)
    for k, v in d.items():
      ans.append(sum(v) / len(v))

    return ans
