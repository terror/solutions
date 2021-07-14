t = int(input())

for _ in range(t):
  n, d, same = int(input()), {}, {}

  for i in range(n):
    toy, c = map(str, input().split())
    if toy in d:
      d[toy] += int(c)
    else:
      d[toy] = int(c)

  for k, v in d.items():
    if v not in same:
      same[v] = [k]
    else:
      same[v].append(k)

  print(len(d.keys()))
  for k, v in sorted(same.items(), reverse=True):
    v = sorted(v) if len(v) > 1 else v
    for i in v:
      print(i, k)
