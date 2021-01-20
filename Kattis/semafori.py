def go(b, s):
    l, r = b
    p = 0
    while 1:
        if not p:
            s -= l
            if s < 0:
                break
        else:
            s -= r
            if s < 0:
                break
        p ^= 1
    return (p, abs(s))


def main():
    N, L = map(int, input().split())
    ans, x = 0, {}
    for _ in range(N):
        D, R, G = map(int, input().split())
        x[D] = [R, G]
    w = 0
    for k, v in x.items():
        ans += abs(ans-k)
        res = go(v, ans+w)
        if not res[0]:
            w += res[1]
    print(ans+abs(max(x.keys()) - L) + w)


if __name__ == '__main__':
    main()
