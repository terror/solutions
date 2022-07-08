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
    q, head, curr = [root], None, None
    while q:
      top = q.pop(0)
      if not head:
        head = LLNode(top.val)
        curr = head
      else:
        curr.next = LLNode(top.val)
        curr = curr.next
      if top.left:
        q.append(top.left)
      if top.right:
        q.append(top.right)
    return head
