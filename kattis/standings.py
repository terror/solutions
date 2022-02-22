for _ in range(int(input())):
  sp = input()
  n = int(input())
  lst = [i for i in range(1, n + 1)]
  new = []
  for i in range(n):
    a, b = list(map(str, input().split()))
    new.append(int(b))
  new.sort()
  s = 0
  for i in range(len(lst)):
    s += abs(lst[i] - new[i])
  print(s)
