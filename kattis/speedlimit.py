# sum += val * hours - prevHours

while True:
  n = int(input())
  if (n < 0): break

  sum = 0
  temp = 0

  for i in range(n):
    line = input().split()
    sum += int(line[0]) * (int(line[1]) - temp)
    temp = int(line[1])

  print("{0} {1}".format(sum, "miles"))
