t = int(input())
for i in range(t):
    n = int(input())
    c = m = 0
    s = list(input())
    for i in s:
        if i == ')':
            c -= 1
        else:
            c += 1
        m = min(c, m)
    print(-m)
