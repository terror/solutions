# class LLNode:
#   def __init__(self, val, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def solve(self, head):
    prev = None
    while head:
      if prev is not None and head.val <= prev:
        return False
      prev = head.val
      head = head.next
    return True
