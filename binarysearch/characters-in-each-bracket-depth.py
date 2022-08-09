class Solution:
  def solve(self, s):
    counter, depth, d = Counter(), 0, {'(': 1, ')': -1}
    for char in s:
      if char in ['(', ')']:
        depth += d[char]
        counter[depth] = counter[depth]
      else:
        counter[depth] += 1
    return list(counter.values())[:-1]
