P, D = list(map(int, input().split()))

d = {}
for _ in range(P):
  i, A, B = list(map(int, input().split()))
  if i in d:
    d[i][0] += A
    d[i][1] += B
  else:
    d[i] = [A, B]

sA = 0
sB = 0
sV = 0
for key, val in sorted(d.items()):
  wA = val[0]
  wB = val[1]
  sV += wA + wB
  w = ((val[0] + val[1]) // 2) + 1

  ans = ''
  if wA > wB:
    ans = 'A'
    wA = val[0] - w
  else:
    ans = 'B'
    wB = val[1] - w
  print('{} {} {}'.format(ans, wA, wB))
  sA += wA
  sB += wB

print('{:.10f}'.format(abs(sA - sB) / sV))
