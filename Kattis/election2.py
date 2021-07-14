n = int(input())
d = {}

for i in range(0, n * 2, 2):
  name = input()
  party = input()
  d[name] = [party, 0]

m = int(input())
for i in range(m):
  b = input()
  for key, val in d.items():
    if b == key:
      val[1] += 1

lst = sorted([val[1] for key, val in d.items()], reverse=True)
p = []
for key, val in d.items():
  if val[1] == max(lst):
    p.append(val[0])

if len(p) > 1:
  print('tie')
else:
  print(*p)
