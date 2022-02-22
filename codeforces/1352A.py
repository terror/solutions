for i in range(int(input())):
  n = str(input())
  s = []
  pos = 0
  counter = 0
  for i in n:
    pos += 1
    if i != '0':
      counter += 1
      summand = i + '0' * (len(n) - pos)
      s.append(summand)
  print(counter)
  print(*s, sep=" ")
