s = list(input())
ans = e = 0
for i, v in enumerate(s[1:]):
    if v.isupper():
        n = 0
        x = (i+1-e)
        while(x % 4 != 0):
            n += 1
            x += 1
        ans += n
        e = i+1
print(ans)
