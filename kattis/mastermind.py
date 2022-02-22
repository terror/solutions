from collections import Counter

n, a, b = list(map(str, input().split()))
r, s, a, b, n, idx = 0, 0, list(a), list(b), int(n), set()

for i in range(n):
  if a[i] == b[i]:
    r += 1
    idx.add(i)

a, b = [a[i] for i in range(len(a)) if i not in idx], [b[i] for i in range(len(b)) if i not in idx]
x = Counter(a)
for i in b:
  if i in x and x[i] > 0:
    x[i] -= 1
    s += 1
print(r, s)
