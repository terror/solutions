n, x = int(input()), sorted(list(map(int, input().split())))
idx, j = [i for i, v in enumerate(x) if i != n - 1 and x[i] != x[i + 1] - 1 or (i == n - 1 and x[i] - 1 == x[i - 1])], 0

for i in idx:
  OP = abs(i - (j - 1))
  if OP > 2:
    print("{}-{}".format(x[j], x[i]), end=" ")
  elif OP == 2:
    print("{} {}".format(x[j], x[i]), end=" ")
  else:
    print("{}".format(x[j]), end=" ")
  j = i + 1
print(*x[j:], end="")
