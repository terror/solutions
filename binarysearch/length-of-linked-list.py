# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def solve(self, node):
    if not node:
      return 0
    ans, curr = 1, node
    while curr.next:
      ans += 1
      curr = curr.next
    return ans

