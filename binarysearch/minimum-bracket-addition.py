class Solution:
  def solve(self, s):
    stack, ans, p = [], 0, {'(': ')'}
    for char in s:
      if char == '(':
        stack.append(char)
      else:
        ans += not stack or not p[stack.pop()] == ')'
    return ans + len(stack)
