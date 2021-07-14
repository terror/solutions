r, c, zr, zc = list(map(int, input().split()))

arr = []
for i in range(r):
  _ = input()
  for j in range(zr):
    arr.append([s * zc for s in _])

print('\n'.join([''.join(['{0}'.format(item) for item in row]) for row in arr]))
