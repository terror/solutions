a, b = list(map(str, input().split()))

for i in a:
  if i in b:
    x, y = a.index(i), b.index(i)
    break

for i in range(len(b)):
  if i == y:
    print(a)
  else:
    l, l[x] = ["."] * len(a), b[i]
    print(''.join(l))
