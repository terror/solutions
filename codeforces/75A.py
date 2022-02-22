n, m = int(input()), int(input())
s = list(str(n + m))
n, m = list(str(n)), list(str(m))

while '0' in s:
  s.remove('0')

while '0' in n:
  n.remove('0')

while '0' in m:
  m.remove('0')

if (int("".join(n)) + int("".join(m)) == int("".join(s))):
  print("YES")
  exit()

print("NO")
