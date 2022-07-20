class Solution:
  def solve(self, s):
    st = []; ans = 0
    for ch in s:
      if ch == '(':
        st.append(ch)
      else:
        if not st:
          ans += 1
        else:
          st.pop()
    return ans + len(st)
