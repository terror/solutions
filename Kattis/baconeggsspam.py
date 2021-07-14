from collections import defaultdict

while True:
  d = defaultdict(list)
  n = int(input())

  if n == 0:
    break

  for _ in range(n):
    name, *items = map(str, input().split())
    for item in items:
      d[item].append(name)

  for k, v in sorted(d.items()):
    print(k, *sorted(v), "\n")
