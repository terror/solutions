import sys

for i in sys.stdin:
  a, b = map(str, i.split())
  if int(a) == 0 and int(b) == 0:
    break
  a, b, ans = [int(i) for i in a], [int(i) for i in b], 0

  while (len(a) < 10):
    a.insert(0, 0)
  while (len(b) < 10):
    b.insert(0, 0)

  for i in range(len(b))[::-1]:
    if b[i] + a[i] >= 10:
      ans += 1
      a[i - 1] += 1

  if ans == 0:
    print("No carry operation.")
  elif ans == 1:
    print("1 carry operation.")
  else:
    print(ans, "carry operations.")
