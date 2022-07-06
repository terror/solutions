class Solution:
  def solve(self, path):
    stack = []
    for op in path:
      if op == '..':
        if not stack:
          continue
        stack.pop()
      elif op == '.':
        continue
      else:
        stack.append(op)
    return stack

