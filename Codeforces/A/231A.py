ans = 0
for i in range(int(input())):
    l = list(map(int, input().split()))
    if l.count(1) >= 2:
        ans += 1
print(ans)
