n, m = map(int, input().split())

relations = [(x, x + 1) for x in [int(input()) for _ in range(m)]]

order = []

for i in range(1, n + 1):
  curr = i
  for u, v in relations:
    if curr in (u, v):
      curr = u if curr != u else v
  order.append((i, curr))

print(*list(map(lambda x: x[0], sorted(order, key = lambda x: x[1]))), sep = '\n')
