s1 = list(input())
s2 = list(input())

if len(s2) != len(s1):
    print("NO")
    exit()

c = 0
idx = []
for i in range(len(s2)):
    if s1[i] != s2[i]:
        c += 1
        idx.append(i)
    if c > 2:
        print("NO")
        exit()

if c != 2:
    print("NO")
    exit()

t = s1[idx[0]]
s1[idx[0]] = s1[idx[1]]
s1[idx[1]] = t

if s1 == s2:
    print("YES")
    exit()

print("NO")
