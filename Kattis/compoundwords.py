import sys

words = []
for i in sys.stdin:
    if i.strip() == '':
        break
    i = list(map(str, i.split()))
    for j in range(len(i)):
        words.append(i[j])

w = set()
for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            w.add(words[i]+words[j])
            w.add(words[j] + words[i])
print(*sorted(w), sep='\n')
