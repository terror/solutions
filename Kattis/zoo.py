import sys

lst = 1
for i in sys.stdin:
  i = int(i)

  if i == 0:
    break
  d = {}

  for _ in range(i):
    x = list(map(str, input().split()))
    if x[len(x) - 1].lower() in d:
      d[x[len(x) - 1].lower()] += 1
    else:
      d[x[len(x) - 1].lower()] = 1

  print("List {}:".format(lst))
  for k, v in sorted(d.items()):
    print("{} | {}".format(k, v))
  lst += 1
