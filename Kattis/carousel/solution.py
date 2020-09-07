import sys

for i in sys.stdin:
    n, m = map(int, i.split())
    if n == 0 and m == 0:
        break
    curr_t, curr_d, mx, p = 0, 0, 0, False
    for i in range(n):
        a, b = map(int, input().split())
        if a > m:
            continue
        if not p:
            curr_t, curr_d, mx = a, b, a/b
            p = True
            continue
        if a/b == mx:
            if a > curr_t:
                curr_t, curr_d = a, b
        if a/b > mx:
            curr_t, curr_d, mx = a, b, a/b
    if curr_t == 0 and curr_d == 0:
        print("No suitable tickets offered")
        continue
    print("Buy {} tickets for ${}".format(curr_t, curr_d))
