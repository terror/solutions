keys = {
    1: list("qwertyuiop"),
    2: list("asdfghjkl"),
    3: list("zxcvbnm")
}


def dis(a, b):
    for k, v in keys.items():
        if a in v:
            a = (v.index(a), k)
        if b in v:
            b = (v.index(b), k)
    return abs(a[1] - b[1]) + abs(a[0] - b[0])


def main():
    for _ in range(int(input())):
        a, b = map(str, input().split())
        ret = []
        for i in range(int(b)):
            w = str(input())
            d = 0
            for j in range(len(w)):
                d += dis(w[j], a[j])
            ret.append([w, d])
        ret = sorted(ret, key=lambda x: (x[1], x[0]))
        for i in ret:
            print(*i)


if __name__ == '__main__':
    main()
