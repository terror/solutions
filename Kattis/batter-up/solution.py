n = int(input())
s = list(map(int, input().split()))

Sum = 0
Count = 0
for i in range(n):
    if s[i] >= 0:
        Sum += s[i]
        Count += 1

print(Sum/Count)
