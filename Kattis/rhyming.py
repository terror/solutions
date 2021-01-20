w, suf = input(), set()
for i in range(int(input())):
    x = set(map(str, input().split()))
    for j in x:
        if w.endswith(j): suf |= x

for i in range(int(input())):
    s, ok = input().split(), False
    for j in suf:
        if s[-1].endswith(j):
            print("YES")
            ok = True
            break
    if not ok: print("NO")
