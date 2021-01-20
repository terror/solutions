import sys

for i in sys.stdin:
    i, s, avg, c = list(map(str, i.split())), [], 0, 0

    for x in i:
        if not x.replace('.', '', 1).isdigit():
            s.append(x)
        else:
            avg += float(x)
            c += 1

    print(avg/c, *s)
