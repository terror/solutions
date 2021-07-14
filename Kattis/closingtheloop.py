from collections import defaultdict

t = int(input())
for CASE in range(t):
  n, d, x = int(input()), defaultdict(list), list(map(str, input().split()))
  for i in range(len(x)):
    d[x[i][-1]].append(int(x[i][0:len(x[i]) - 1]))
  tot, i = 0, 0
  d['R'].sort()
  d['B'].sort()
  while d['B'] and d['R']:
    if i > 0 and i % 2 == 0:
      d['B'].pop()
      d['R'].pop()
      tot -= 2
      if not d['R'] or not d['B']: break
    if i % 2 == 0: tot += d['R'][-1]
    else: tot += d['B'][-1]
    i += 1
  print("Case #{}: {}".format(CASE + 1, tot))
