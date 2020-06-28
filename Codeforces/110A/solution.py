n = list(input())

c = 0
for i in n:
    if i == '7' or i == '4':
        c += 1

if c == 7 or c == 4:
    print('YES')
else:
    print('NO')
