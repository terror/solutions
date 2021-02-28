from math import pi


def main():
    d = {v: i for i, v in enumerate([i for i in range(65, 91)] + [32, 39])}
    for _ in range(int(input())):
        i, ans = list(input()), 0

        start = d[ord(i[0])]
        for ch in i[1:]:
            nxt = d[ord(ch)]
            ans += min(abs(start - nxt), 28 - (abs(start - nxt))) * pi / 7
            start = nxt

        print(ans + (len(i)))


if __name__ == "__main__":
    main()
