while True:
    n = int(input())
    if n == 0:
        break
    l1, l2, index, s = [int(input()) for i in range(n)], sorted(
        [int(input()) for i in range(n)]), [], set()
    for i in l2:
        vals = []
        for j in l1:
            if j not in s:
                vals.append(j)
        index.append(l1.index(min(vals)))
        s.add(min(vals))
    ans, c = [0]*n, 0
    for i in index:
        ans[i] = l2[c]
        c += 1
    for i in ans:
        print(i)
    print("\n")
