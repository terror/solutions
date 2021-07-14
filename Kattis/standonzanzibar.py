for _ in range(int(input())):
  tot = 0
  lst = list(map(int, input().split()))
  for i in range(1, len(lst)):
    if lst[i] > lst[i - 1] * 2:
      tot += (lst[i] - 2 * lst[i - 1])
  print(tot)
