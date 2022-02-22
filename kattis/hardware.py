import sys

x, l = sys.stdin.readlines(), 1

for _ in range(int(x[0])):
  print("{}\n {}".format(x[l], x[l + 1]))

  d, l, c = {i: 0 for i in range(10)}, l + 2, 0

  while (l < len(x) and (x[l][0] == '+' or x[l][0].isdigit())):
    if x[l][0] == '+':
      x[l] = x[l].split()
      for i in range(int(x[l][1]), int(x[l][2]) + 1, int(x[l][3])):
        for j in str(i):
          d[int(j)] += 1
    else:
      for i in x[l][:len(x[l]) - 1]:
        d[int(i)] += 1
    l += 1

  for k, v in sorted(d.items()):
    c += v
    print("Make {} digit {}".format(v, k))
  print("In total {} {}".format(c, "digits" if c > 1 else "digit"))
