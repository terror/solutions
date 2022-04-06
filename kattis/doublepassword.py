a, b = input(), input()

if a == b:
  print(1)
  exit()

ans = 1

for i, c in enumerate(a):
  if c == b[i]:
    continue
  ans *= 2

print(ans)
