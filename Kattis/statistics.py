# warmup
import sys
c = 1
for i in sys.stdin:
    i = list(map(int, i.split()))
    i.remove(i[0])
    print("Case {0}: {1} {2} {3}".format(c, min(i), max(i), max(i) - min(i)))
    c += 1
