n = int(input())

s = set()
for i in range(n):
  t = input().lower()
  t = t.replace('-', ' ')
  s.add(t)

print(len(s))
