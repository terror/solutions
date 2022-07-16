class Solution:
  def solve(self, words, letters):
    c = Counter(letters); ans = 0
    for word in words:
      d = Counter(word)
      if all(c[x] >= d[x] for x in word):
        ans = max(len(word), ans)
    return ans
