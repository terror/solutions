ans = 0
for i in range(1, 999):
  for j in range(1, 999):
    ans = max(ans, i * j * (str(i * j) == str(i * j)[::-1]))
print(ans)
