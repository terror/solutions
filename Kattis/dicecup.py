a, b = map(int, input().split())

if a != b:
    x = abs(a-b) + 1
    y = min(a, b) + 1
    for i in range(y, x+y):
        print(i)
else:
    print(a+1)
