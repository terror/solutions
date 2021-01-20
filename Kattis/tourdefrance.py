import sys

for i in sys.stdin:
    if i.rstrip() == '0':
        break
    n, m = map(int, i.split())
    f = sorted(list(map(int, input().split())))
    r = sorted(list(map(int, input().split())))
    ans, mx = [], 0
    for j in f:
        for k in r:
            ans.append(k/j)
    ans.sort()
    for i in range(1, len(ans)):
        mx = max(mx, ans[i]/ans[i-1])
    print("{:.2f}".format(mx))
