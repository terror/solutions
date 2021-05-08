import sys


def main():
    d = {}

    for i in sys.stdin:
        q, *x = list(map(str, i.split()))

        if q == 'define':
            d[x[1]] = int(x[0])

        if q == 'eval':
            print('undefined' if not all(k in d for k in (x[0], x[2])) else ('true' if eval(x, d) else 'false'))

def eval(i, d) -> bool:
    a, b, c = i

    return {
        '>': lambda a, b: d[a] > d[b],
        '<': lambda a, b: d[a] < d[b],
        '=': lambda a, b: d[a] == d[b]
    }[b](a, c)

if __name__ == '__main__':
    main()
