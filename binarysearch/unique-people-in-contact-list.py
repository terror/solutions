class Solution:
  def solve(self, contacts):
    c, ans = Counter(), 0
    for contact in contacts:
      ans += all(c[email] == 0 for email in contact)
      for email in contact:
        c[email] += 1
    return ans
