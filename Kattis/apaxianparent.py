# ad hoc
Y, P = list(map(str, input().split()))
ans = ''
v = ['a', 'i', 'o', 'u']
temp = list(Y)

if temp[len(temp) - 1] == 'e':
    ans += (Y+'x'+P)
elif temp[len(temp) - 1] in v:
    temp.pop()
    t = ''
    for i in temp:
        t += i
    ans += (t+'ex'+P)
elif temp[len(temp) - 2] == 'e' and temp[len(temp) - 1] == 'x':
    ans += (Y+P)
else:
    ans += (Y+'ex'+P)

print(ans)
