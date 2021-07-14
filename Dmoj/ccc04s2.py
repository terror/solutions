n, k = map(int, input().split())
s, r, w = [0] * int(2e5), [1] * int(2e5), [0] * int(2e5)

for i in range(k):
  x = list(map(int, input().split()))
  for j in range(n):
    s[j] += x[j]
  for j in range(n):
    c = 1
    for k in range(n):
      if k != j and s[k] > s[j]: c += 1
      if c > w[j]: w[j] = c
      r[j] = c

for i in range(n):
  if r[i] == 1: print("Yodeller {} is the TopYodeller: score {}, worst rank {}".format(i + 1, s[i], w[i]))
