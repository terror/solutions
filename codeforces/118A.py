v = 'aoyeui'
s = list(input())
new = []
for i in range(len(s)):
  if s[i].lower() not in v:
    new.append(s[i].lower())

for i in range(len(new) * 2):
  if i % 2 == 0:
    new.insert(i, '.')
print("".join(new))
