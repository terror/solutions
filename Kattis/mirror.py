t = int(input())

case = 1
for i in range(t):
    r, c = list(map(int, input().split()))
    arr = []
    for i in range(r):
        arr.append([i for i in input()])
    for i in range(len(arr)):
        arr[i].reverse()
    print('Test {}'.format(case))
    for i in range(len(arr)-1, -1, -1):
        print(''.join(i for i in arr[i]))
    case += 1
