d = {
  '2': ['a', 'b', 'c'],
  '3': ['d', 'e', 'f'],
  '4': ['g', 'h', 'i'],
  '5': ['j', 'k', 'l'],
  '6': ['m', 'n', 'o'],
  '7': ['p', 'q', 'r', 's'],
  '8': ['t', 'u', 'v'],
  '9': ['w', 'x', 'y', 'z']
}

temp = {}
for i in range(int(input())):
  s = ''
  for ch in input():
    for key, val in d.items():
      if ch in val:
        s += key
  if s in temp:
    temp[s] += 1
  else:
    temp[s] = 1

s = input()
print(temp[s] if s in temp else 0)
