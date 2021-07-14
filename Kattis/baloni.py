n, a, arr = int(input()), list(map(int, input().split())), [0] * 1000000

for i in range(n):
  if arr[a[i]] != 0:
    arr[a[i]] -= 1
  arr[a[i] - 1] += 1
print(sum(arr))
