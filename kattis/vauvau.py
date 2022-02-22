abcd = list(map(int, input().split()))
pmg = list(map(int, input().split()))

for i in range(len(pmg)):
  dogs = 0
  for j in range(0, len(abcd), 2):
    time = pmg[i] % (abcd[j] + abcd[j + 1])
    if time <= abcd[j] and time != 0:
      dogs += 1
  if dogs == 2:
    print("both")
  elif dogs == 1:
    print("one")
  else:
    print("none")
