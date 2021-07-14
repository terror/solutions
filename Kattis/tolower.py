p, t = list(map(int, input().split()))
solved = 0
for i in range(p):
  temp = 0
  for i in range(t):
    a = input()
    b = a[0].lower() + a[1:]
    if not any(x.isupper() for x in b):
      temp += 1
      if temp == t:
        solved += 1
        break
print(solved)
