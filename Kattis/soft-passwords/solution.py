def main():
    s = input()
    p = input()
    if solve(s, p):
        print("Yes")
    else:
        print("No")


def solve(s, p):
    if s == p:
        return True

    opposite = ''.join(c.lower() if c.isupper() else c.upper() for c in p)
    if opposite == s:
        return True
    else:
        temp = s
        s = list(s)
        if p + s[len(s) - 1] == temp and s[len(s) - 1].isdigit():
            return True
        elif s[0] + p == temp and s[0].isdigit():
            return True
        else:
            return False


main()
