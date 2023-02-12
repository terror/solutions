import sys

a, b, c = map(int, input().split())

ans = sys.maxsize

ops = {
  '*': lambda x, y: x * y,
  '+': lambda x, y: x + y,
  '-': lambda x, y: x - y,
  '/': lambda x, y: x // y
}

for x in ops:
  if x == '/' and a % b != 0:
    continue

  r1 = ops[x](a, b)

  for y in ops:
    if y == '/' and r1 % c != 0:
      continue

    result = ops[y](r1, c)

    if result >= 0:
      ans = min(ans, result)

print(ans)
