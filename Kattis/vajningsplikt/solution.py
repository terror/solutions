def c1(a, b):
    if a == 'North' and b == 'South' or (b == 'North' and a == 'South'):
        return 1
    if a == 'East' and b == 'West' or (a == 'West' and b == 'East'):
        return 1
    return 0


def r(a):
    if a == 'South':
        return 'East'
    if a == 'North':
        return 'West'
    if a == 'West':
        return 'South'
    if a == 'East':
        return 'North'


def r2(a):
    if a == 'South':
        return 'West'
    if a == 'North':
        return 'East'
    if a == 'West':
        return 'North'
    if a == 'East':
        return 'South'


def op(a):
    if a == 'South':
        return 'North'
    if a == 'North':
        return 'South'
    if a == 'West':
        return 'East'
    if a == 'East':
        return 'West'


def main():
    a, b, c = map(str, input().split())

    if c1(a, b) and c == r(a):
        return 1

    if b == r2(a) and (op(a) == c or c == r(a)):
        return 1

    return 0


if __name__ == '__main__':
    print("Yes" if main() == 1 else "No")
