class Solution:
  def solve(self, s, t):
    if s == t:
      return True

    if len(s) != len(t):
      return False

    a, b = Counter(s), Counter(t)

    seen = []
    for i in range(len(s)):
      if (s[i], t[i]) in seen:
        continue
      if a[s[i]] != b[t[i]]:
        return False
      seen.append((s[i], t[i]))

    return True
