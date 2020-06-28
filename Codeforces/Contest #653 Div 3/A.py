import math
t = int(input())
for i in range(t):
    y, x, n = list(map(int, input().split()))
    temp = n//y
    if y*temp+x <= n:
        print(y*temp+x)
    else:
        print(y*(temp-1)+x)
