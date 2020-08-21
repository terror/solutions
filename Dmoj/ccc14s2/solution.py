n, s1, s2, i, s = int(input()), list(
    input().split()), list(input().split()), 0, "good"

while i < n:
    pos = s1.index(s2[i])
    if s1[i] != s2[pos] or pos == i:
        s = "bad"
        break
    i += 1
print(s)
