for case in range(1, int(input())+1):
    N, T = map(int, input().split())
    E, d, pos, ans = int(input()), {i: [] for i in range(1, N+1)}, True, [0]*N
    for _ in range(E):
        H, P = map(int, input().split())
        d[H].append(P)
    for k, v in d.items():
        if k == T:
            continue
        v.sort(reverse=True)
        c = 0
        while len(v):
            if v[0] == 0:
                pos = False
                break
            else:
                c, x = c+1, v[0]-1
                v.remove(v[0])
                while x > 0 and len(v):
                    v.remove(v[-1])
                    x -= 1
        ans[k-1] = c
    if not pos:
        print("Case #{}: IMPOSSIBLE".format(case), end="")
    else:
        print("CASE #{}: ".format(case), end="")
        for i in ans:
            print(i, end=" ")
    print()
