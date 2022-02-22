import sys

for i in sys.stdin:
  N, M = map(int, i.split())

  if N == 0 and M == 0:
    break

  grid, ans, new = [list(input()) for i in range(N)], [], []

  for i in range(M):
    new.append([grid[j][i] for j in range(N)])
  for i in range(M):
    new[i] = "".join(new[i])

  # ignore case
  new = sorted(new, key=str.casefold)

  for i in range(N):
    ans.append([new[j][i] for j in range(M)])
  for i in ans:
    print("".join(i))
  print()
