scores = list(input())
a = 0
b = 0

for i in range(len(scores)):
    if scores[i] == 'A':
        a += int(scores[i+1])

    if scores[i] == 'B':
        b += int(scores[i+1])

if a > b:
    print("A")
else:
    print("B")
