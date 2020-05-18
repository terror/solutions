n = int(input())
lst = sorted([int(input()) for i in range(n)])

ans = sorted(set(range(lst[0], lst[len(lst) - 1])).difference(lst))

if lst[0] > 1:
    for i in range(1, lst[0]):
        ans.append(i)


if(len(ans) != 0):
    print(*sorted(ans), sep='\n')
else:
    print("good job")
