m = 0
s = 0
for i in range(int(input())):
  M, S = list(map(int, input().split()))
  m += M
  s += S

if (s / (m * 60)) <= 1:
  print("measurement error")
else:
  print(s / (m * 60))
