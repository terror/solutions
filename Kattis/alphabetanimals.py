s, d, p = input()[-1], {i: 0 for i in list("abcdefghijklmnopqrstuvwxyz")}, []

for i in range(int(input())):
    t = input()
    d[t[0]] = 1
    if t[0] == s: p.append(t)

if not p:
    print("?")
    exit()

for i in p:
    if not d[i[-1]] or (s == p[0][-1] and len(p) == 1):
        print("{}!".format(i))
        exit()

print(p[0])
