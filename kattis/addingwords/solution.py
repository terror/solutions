import sys
d = {}

for i in sys.stdin:
    i = list(map(str, i.split()))
    if i[0] == 'def':
        d[i[1]] = i[2]
    if i[0] == 'calc':
        ok = True
        i.remove(i[0])
        temp = i.copy()
        ans = 'unknown'
        for j in range(len(i)):
            if i[j] != '+' and i[j] != '-' and i[j] != '=':
                if i[j] in d:
                    i[j] = d[i[j]]
                else:
                    print(*temp, ans)
                    ok = False
                    break
        if not ok:
            continue
        s = int(i[0])
        for k in range(1, len(i)):
            if i[k] == '+':
                s += int(i[k+1])
            if i[k] == '-':
                s -= int(i[k+1])
        for key, val in d.items():
            if s == int(val):
                ans = key
        print(*temp, ans)
    if i[0] == 'clear':
        d.clear()
