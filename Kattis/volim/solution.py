K = int(input())
t = 210

for i in range(int(input())):
    s = input().split()
    t -= int(s[0])
    if t < 0:
        break
    if s[1] != 'T':
        continue
    K += 1
if K % 8 == 0:
    K = 8
else:
    K %= 8
print(K)
