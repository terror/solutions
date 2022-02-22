tot = 0; t = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
for i, ch in enumerate(''.join(input().split('-'))):
  tot += int(ch) * t[i]
print(int(tot % 11 == 0))
