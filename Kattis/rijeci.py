a = 1
b = 0
for i in range(int(input())):
  t = b
  b = a
  a += t
print("{0} {1}".format(a - b, b))
