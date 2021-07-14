n = int(input())

for i in range(n):
  a = list(map(int, input().split()))
  a.remove(a[0])
  b = sorted(a)
  for i in range(len(a)):
    if a[i] != b[i]:
      if a.index(a[i]) == a.index(b[i]):
        print(i)
      elif a[len(b) - 1] == b[len(b) - 1]:
        print(a.index(b[0]) + 1)
      else:
        print(a.index(b[len(b) - 1]) + 1)
      break
