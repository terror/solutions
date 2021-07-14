n = int(input())
arr = list(map(int, input().split()))

gis = []
gis.append(arr[0])
m = arr[0]
for i in range(1, n):
  if arr[i] > m:
    gis.append(arr[i])
    m = arr[i]
print(len(gis))
print(*gis)
