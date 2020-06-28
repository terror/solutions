s = input()
r = 0
for i in range(len(s)):
    if(i % 3 == 0 and s[i] != 'P'):
        r = r + 1
    if(i % 3 == 1 and s[i] != 'E'):
        r = r + 1
    if(i % 3 == 2 and s[i] != 'R'):
        r = r + 1

print(r)
