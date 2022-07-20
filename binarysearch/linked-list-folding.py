# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def solve(self, node):
    l = []

    while node:
      l.append(node.val)
      node = node.next

    h = t = None

    i = len(l) // 2
    if len(l) & 1:
      h = LLNode(l[i])
      t = h
      i -= 1
    else:
      i -= 1

    while i >= 0:
      print(i)
      if h is None:
        h = LLNode(l[i] + l[len(l) - i - 1])
        t = h
      else:
        t.next = LLNode(l[i] + l[len(l) - i - 1])
        t = t.next
      i -= 1
    return h
