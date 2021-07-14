a = list(map(int, input().split()))
b = sorted(list(map(int, input().split())))
p = a[1]

i = 1
while i < a[0]:
  if (b[i] + b[i - 1] > p):
    break
  i += 1

print(i)
