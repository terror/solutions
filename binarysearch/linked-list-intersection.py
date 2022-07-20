# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def solve(self, l0, l1):
    h = r = None
    while l0 is not None and l1 is not None:
      if l0.val == l1.val:
        if h is None:
          h = LLNode(l0.val)
          r = h
        else:
          h.next = LLNode(l0.val)
          h = h.next
        # advance both
        l0 = l0.next
        l1 = l1.next
      else:
        if l0.val < l1.val:
          l0 = l0.next
        else:
          l1 = l1.next
    return r
