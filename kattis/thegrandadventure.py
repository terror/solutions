n = int(input())

for i in range(n):
  stack = []
  line = input()
  fail = False
  for j in line:
    if j == 't':
      if not stack or stack.pop() != '|':
        fail = True
        break
    if j == 'j':
      if not stack or stack.pop() != '*':
        fail = True
        break
    if j == 'b':
      if not stack or stack.pop() != '$':
        fail = True
        break
    if j != '.' and j != 'b' and j != 't' and j != 'j':
      stack.append(j)
  if stack:
    fail = True
  if fail:
    print('NO')
  else:
    print('YES')
