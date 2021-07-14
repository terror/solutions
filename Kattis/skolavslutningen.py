n, m, k = map(int, input().split())
cols, d = list(zip(*[list(input()) for i in range(n)])), {}
for i in range(len(cols)):
  for j in cols[i]:
    if j in d:
      for i in cols[i]:
        d[i] = d[j]
      break
    else:
      d[j] = i
print(len(set(d.values())))
