n = int(input())
# fix run time err
if (n > 30):
  n = 30
sum = 1
factorial = 1

for i in range(1, n + 1):
  factorial *= i
  sum += (1.0 / factorial)

print(sum)
