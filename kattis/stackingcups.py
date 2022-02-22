d = {}
b = []

for i in range(int(input())):
  a = input().split()
  if a[0].isdigit():
    c = a[1]
    n = int(a[0]) // 2
  else:
    c = a[0]
    n = int(a[1])
  d[n] = c
  b.append(n)

b.sort()
for j in b:
  print(d.get(j))
