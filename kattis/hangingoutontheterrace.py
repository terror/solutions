l, x = list(map(int, input().split()))
count = 0
curr = 0
for i in range(x):
  action, p = input().split()
  if action == 'enter':
    curr += int(p)
    if curr > l:
      curr -= int(p)
      count += 1
  else:
    curr -= int(p)
print(count)
