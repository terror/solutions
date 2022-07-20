# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def solve(self, node):
    h = t = None
    while node:
      if h is None:
        h = Tree(node.val)
        t = h
      else:
        if node.val < t.val:
          t.left = Tree(node.val)
          t = t.left
        else:
          t.right = Tree(node.val)
          t = t.right
      node = node.next
    return h
