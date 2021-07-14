d = set()

for i in range(int(input())):
  I = input().split('-> ')
  if len(I) == 1:
    d.add(I[1])
    continue
  a, k = I
  for aa in a.split():
    if aa not in d:
      print(i + 1)
      exit()
  d.add(k)
print('correct')
