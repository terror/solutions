n = int(input())
m = list(input())
f = list(input())

same = 0
for i in range(len(m)):
  if m[i] == f[i]:
    same += 1

if same > n:
  print(n + (len(m) - same))
else:
  print(same + (len(m) - n))
