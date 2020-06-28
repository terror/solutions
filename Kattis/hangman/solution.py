s = input()
g = list(input())
m = 0

for i in range(len(g)):
    if g[i] in s:
        s = s.replace(g[i], '')
        if len(s) == 0:
            break
    else:
        m += 1

if m < 10:
    print("WIN")
else:
    print("LOSE")
