class Solution:
  def solve(self, words):
    c = Counter()
    for i in range(len(words)):
      for key in c:
        if words[i] in key and len(key) - len(words[i]) == len(words[i]):
          c[key] += 1; break
      else: c[words[i] + words[i]] += 1
    return len(c)
