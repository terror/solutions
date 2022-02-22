n = int(input())
for i in range(n):
  tot = 0
  k, *arr = list(map(int, input().split()))
  # insertion sort
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
      tot += 1
    arr[j + 1] = key
  print("{0} {1}".format(k, tot))
