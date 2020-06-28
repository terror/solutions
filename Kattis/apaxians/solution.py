line = input()
ans = []
t = ''
for l in line:
    if t != l:
        ans.append(l)
    t = l
print(''.join(ans))
