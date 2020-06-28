n = int(input())
stack = []
c = list(map(int, input().split()))
for i in range(n*2):
    t = c[i]
    if not stack or stack[len(stack)-1] != t:
        stack.append(t)
    else:
        stack.pop()
if stack:
    print('impossible')
else:
    print(n*2)
