for i in range(int(input())):
  a, b = list(map(int, input().split()))
  if a % b == 0:
    print(0)
  else:
    print(b - a % b)
