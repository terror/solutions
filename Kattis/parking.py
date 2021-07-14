a, b, c = list(map(int, input().split()))
d, t, ans = {}, 1, 0

for i in range(3):
  x, y = list(map(int, input().split()))
  d[i] = [x, y]

while t <= 100:
  curr = 0
  for key, val in d.items():
    if t >= val[0] and t < val[1]:
      curr += 1
  if curr == 3:
    ans += 3 * c
  elif curr == 2:
    ans += 2 * b
  elif curr == 1:
    ans += a
  else:
    ans += 0
  t += 1

print(ans)
