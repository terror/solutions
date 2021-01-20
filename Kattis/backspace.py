l = list(input())
c = 0
for i in range(len(l) - 1, -1, -1):
    if l[i] == '<':
        l[i] = ''
        c += 1
    elif c > 0:
        l[i] = ''
        c -= 1
print(''.join(l))
