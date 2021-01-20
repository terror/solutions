scores = []
for i in range(5):
    s = list(map(int, input().split()))
    scores.append(sum(s))
print("{0} {1}".format((scores.index(max(scores)) + 1), max(scores)))
