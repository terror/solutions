# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def x(root, distance, level, mp):
  if not root:
    return

  if distance in mp:
    mp[distance].append((root.val, level))
  else:
    mp[distance] = [(root.val, level)]

  level -= 1
  x(root.left, distance - 1, level, mp)
  x(root.right, distance + 1, level, mp)

class Solution:
  def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    mp = {}
    distance, level = 0, 1000000
    x(root, distance, level, mp)

    ans = []
    for i in sorted(mp.keys()):
      t = {}

      for key, val in mp[i]:
        if val in t:
          t[val].append(key)
        else:
          t[val] = [key]

      temp = []
      for key, val in sorted(t.items(), reverse=True):
        for i in sorted(val):
          temp.append(i)

      ans.append(temp)

    return ans
