import sys

for i in sys.stdin:
    n1, n2 = list(map(int, i.split()))
    if n1 == 0:
        break
    a = n1//n2
    b = n1 % n2
    print("{0} {1} / {2}".format(a, b, n2))
