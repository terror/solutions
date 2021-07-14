n, b = input().split()
Sum = 0

d = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}

for i in range(int(n) * 4):
  a = list(input())
  if a[1] == b:
    Sum += d[a[0]]
  else:
    if a[0] == 'J':
      Sum += 2
    elif a[0] == '9':
      Sum += 0
    else:
      Sum += d[a[0]]

print(Sum)
