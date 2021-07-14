a = 0
b = 1
c = 0
Sum = 0
n = []

for i in range(32):
  c = a + b
  n.append(c)
  a = b
  b = c

for i in range(len(n)):
  if n[i] % 2 == 0:
    Sum += n[i]

print(Sum)
