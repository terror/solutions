from collections import Counter

n, c = list(map(int, input().split()))
arr = list(map(int, input().split()))

count = {v: [k for k in Counter(arr) if Counter(arr)[k] == v] for v in set(Counter(arr).values())}

new = []

for key, val in sorted(count.items(), reverse=True):
  if len(val) > 1:
    index = 0
    arr = list(set(arr))
    for i in range(len(arr)):
      if arr[i] in val:
        for i in range(key):
          new.append(val[index])
        index += 1
  else:
    for i in range(key):
      new.append(val[0])

print(*new)
