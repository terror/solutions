n = input()
d = {'000': 0,
     '001': 1,
     '010': 2,
     '011': 3,
     '100': 4,
     '101': 5,
     '110': 6,
     '111': 7}

while len(n) % 3 != 0:
    n = '0' + n

n = [n[i:i+3] for i in range(0, len(n), 3)]
ans = []

for i in range(len(n)):
    if n[i] in d:
        ans.append(d[n[i]])

print(*ans, sep='')
