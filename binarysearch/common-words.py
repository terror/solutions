class Solution:
  def solve(self, s0, s1):
    a, b = Counter(map(lambda x: x.lower(), s0.split())), Counter(map(lambda x: x.lower(), s1.split()))
    ans = 0
    for k in a:
      if k in b:
        ans += 1
    return ans
