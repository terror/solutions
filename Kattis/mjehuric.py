lst = list(map(int, input().split()))

for i in range(len(lst) - 1):
  for j in range(0, len(lst) - i - 1):
    if lst[j] > lst[j + 1]:
      lst[j], lst[j + 1] = lst[j + 1], lst[j]
      print(*lst)
