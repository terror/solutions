c = 0
for i in range(int(input())):
  s = input().lower()
  if "pink" in s:
    c += 1
  elif "rose" in s:
    c += 1

if c:
  print(c)
else:
  print("I must watch Star Wars with my daughter")
