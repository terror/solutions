# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def solve(self, node):
    h = node
    while h:
      v = h.val
      t = h
      while v > 0:
        if t.next is None:
          t = None
          break
        t = t.next
        v -= 1
      h.next = t
      h = h.next
    return node
