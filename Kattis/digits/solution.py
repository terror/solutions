def main():
    while True:
        s = input()
        if s == 'END':
            break
        else:
            print(recurr(1, s))


def recurr(c, s):
    size = len(s)
    if str(size) == s:
        return c
    return recurr(c + 1, str(size))


main()
