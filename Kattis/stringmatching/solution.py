import sys

def main():
    x = sys.stdin.readlines()
    for i in range(0, len(x), 2): print(*m(x[i+1].rstrip(), x[i].rstrip()))

def m(s, p):
    x, g, idx = part(p), 0, []
    for i in range(len(s)):
        while g and p[g] != s[i]: g = x[g - 1]
        g += p[g] == s[i]
        if g == len(x):
            idx.append(i + 1 - g)
            g = x[g - 1]
    return idx

def part(s):
    g, x = 0, [0] * len(s)
    for i in range(1, len(s)):
        while g and (s[g] != s[i]): g = x[g - 1]
        x[i] = g = g + (s[g] == s[i])
    return x

main()
