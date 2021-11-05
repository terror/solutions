import sys
from collections import Counter

n, m = list(map(int, input().split()))
d = {}
ans = []

for _ in range(n):
  a, b = map(str, input().split())
  d[a] = int(b)

for _ in range(m):
  money = 0
  while True:
    i = sys.stdin.readline()
    if i.rstrip() == '.':
      ans.append(money)
      break
    else:
      for key, val in Counter(i.split()).items():
        if key in d: money += val * d[key]

print(*ans, sep='\n')
