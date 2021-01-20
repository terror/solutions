import sys


def main():
    for i in sys.stdin:
        a, b = list(map(int, i.split()))
        if a == 0 and b == 0:
            break
        else:
            print(solve(a, b))


def solve(a, b):
    if a + b == 13:
        return 'Never speak again.'
    if a == b:
        return 'Undecided.'
    if a > b:
        return 'To the convention.'
    if a < b:
        return 'Left beehind.'


main()
