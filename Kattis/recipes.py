from collections import defaultdict


def main():
    for case in range(1, int(input())+1):
        R, P, D = map(int, input().split())
        print("Recipe # {}".format(case))
        solve(R, P, D)


def solve(R, P, D):
    s, d = D/P, defaultdict(list)
    for _ in range(R):
        n, w, p = map(str, input().split())
        d[n].append(w)
        d[n].append(p)
    x = 0
    for k, v in d.items():
        if float(v[1]) == 100.0: x = s*float(v[0])
    for k, v in d.items(): print(k, "{:.1f}".format(float(v[1])*x/100))
    print('----------------------------------------')


if __name__ == '__main__':
    main()
