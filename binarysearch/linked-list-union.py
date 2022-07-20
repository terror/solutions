# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def solve(self, ll0, ll1):
    a, b = set(), set()
    while ll0:
      a.add(ll0.val)
      ll0 = ll0.next
    while ll1:
      b.add(ll1.val)
      ll1 = ll1.next
    h = t = None
    for u in sorted(list(a.union(b))):
      if h is None:
        h = LLNode(u)
        t = h
      else:
        t.next = LLNode(u)
        t = t.next
    return h
