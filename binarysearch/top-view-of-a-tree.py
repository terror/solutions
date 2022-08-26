# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def solve(self, root):
    q, s = deque([(root, 0)]), {}
    while q:
      node, x = q.popleft()
      if x not in s:
        s[x] = node.val
      if node.left:
        q.append((node.left, x - 1))
      if node.right:
        q.append((node.right, x + 1))
    return [s[k] for k in sorted(s)]
