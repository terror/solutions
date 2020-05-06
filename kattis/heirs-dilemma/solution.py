def solve(n):
    c = 0
    a = [int(x) for x in str(n)]
    if len(a) == len(set(a)):
        for j in range(len(a)):
            if a[j] != 0 and n % a[j] == 0:
                c += 1
                if c == len(a):
                    return True
    return False


n = list(map(int, input().split()))
counter = 0
for i in range(n[0], n[1]):
    if solve(i):
        counter += 1

print(counter)
