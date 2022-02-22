t = int(input())

for i in range(t):
  n = list(map(int, input().split()))[1:]
  diff = [n[i] - n[i + 1] for i in range(len(n) - 1)]
  if len(set(diff)) == 1: print("arithmetic")
  else:
    n.sort()
    newdiff = [n[i] - n[i + 1] for i in range(len(n) - 1)]
    print("permuted arithmetic" if len(set(newdiff)) == 1 else "non-arithmetic")
