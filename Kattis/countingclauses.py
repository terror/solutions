n, m = list(map(int, input().split()))

for i in range(n):
    c = list(map(int, input().split()))

if n >= 8:
    print('satisfactory')
else:
    print('unsatisfactory')
