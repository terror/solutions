import sys
for i in sys.stdin:
  if i.rstrip() == '':
    break

  i = int(i)
  s = []
  q = []
  pq = []

  p = [1] * 3

  for j in range(i):
    a, b = list(map(int, input().split()))
    if a == 1:
      s.append(b)
      q.append(b)
      pq.append(b)
    else:
      if p[0] == 1:
        if s:
          if s[len(s) - 1] != b:
            p[0] = 0
          else:
            del s[len(s) - 1]
        else:
          p[0] = 0
      if p[1] == 1:
        if q:
          if q[0] != b:
            p[1] = 0
          else:
            del q[0]
        else:
          p[1] = 0
      if p[2] == 1:
        if pq:
          if max(pq) != b:
            p[2] = 0
          else:
            del pq[pq.index(max(pq))]
        else:
          p[2] = 0

  count = sum(p)

  if count > 1:
    print('not sure')
  elif count == 0:
    print('impossible')
  else:
    if p[0] == 1:
      print('stack')
    else:
      print('queue') if p[1] == 1 else print('priority queue')
