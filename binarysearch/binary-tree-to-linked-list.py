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
  def solve(self, root):
    h = t = None

    def add(value):
      nonlocal h, t
      if h is None:
        h = LLNode(value)
        t = h
      else:
        t.next = LLNode(value)
        t = t.next

    def traverse(root):
      if root:
        if root.left:
          traverse(root.left)
        add(root.val)
        if root.right:
          traverse(root.right)

    traverse(root)

    return h
