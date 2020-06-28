n = int(input())
ar = list(map(int, input().split()))

new = [1]*n
for i in range(len(ar)):
    new[ar[i]+1] = i+2
print(*new)
