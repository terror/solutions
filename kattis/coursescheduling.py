from collections import Counter, defaultdict

ret, d = Counter(), defaultdict(dict)
for _ in range(int(input())):
  a, b, c = map(str, input().split())
  n = a + b
  if c in d[n]: continue
  ret[c] += 1
  d[n][c] = 1
for k in sorted(ret.keys()):
  print(k, ret[k])
