W, P = map(int, input().split())
part = list(map(int, input().split()))

part.append(0)
part.append(W)
part.sort()

ans = set()

for i in range(len(part)):
  curr = part[i]
  for j in range(len(part)):
    if j != i:
      ans.add(abs(part[i] - part[j]))
print(*sorted(list(ans)))
