from math import sqrt

i = j = 0
while i <= 10001:
  j += 1
  i += all(map(lambda i: j % i, range(2, int(sqrt(j)) + 1)))

print(j)
