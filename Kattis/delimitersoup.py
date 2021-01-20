n = int(input())
lst = [i for i in input()]

stack = []
b = ["(", "{", "["]
ans = ''
m = True

for i in range(len(lst)):
    if lst[i] == ' ':
        continue
    if lst[i] in b:
        stack.append(lst[i])
    else:
        if not stack:
            ans = lst[i]
            m = False
            break
        if stack[len(stack)-1] == '(':
            if lst[i] != ')':
                ans = lst[i]
                m = False
                break
        if stack[len(stack)-1] == '{':
            if lst[i] != '}':
                ans = lst[i]
                m = False
                break
        if stack[len(stack)-1] == '[':
            if lst[i] != ']':
                ans = lst[i]
                m = False
                break
        stack.pop()

if not m:
    print(ans, i)
else:
    print('ok so far')
