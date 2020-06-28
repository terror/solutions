import sys


def main():
    d = {}

    for i in sys.stdin:
        i = list(map(str, i.split()))
        if i[0] == 'define':
            d[i[2]] = int(i[1])
        if i[0] == 'eval':
            print(eval(i, d))


def eval(i, d):
    if i[1] not in d or i[3] not in d:
        return 'undefined'
    n1 = d[i[1]]
    n2 = d[i[3]]
    if i[2] == '<':
        if n1 < n2:
            return 'true'
        else:
            return 'false'
    if i[2] == '>':
        if n1 > n2:
            return 'true'
        else:
            return 'false'
    if i[2] == '=':
        if n1 == n2:
            return 'true'
        else:
            return 'false'


main()
