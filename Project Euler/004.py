Max = 0
for i in range(999):
  for j in range(999):
    s = str(i * j)
    if i * j > Max and s == s[::-1]:
      Max = i * j
print(Max)
