d = {
    '0': [" "],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

n = int(input())

for i in range(n):
  t = input()
  prev = ''
  print("Case #{}: ".format(i + 1), end='')
  for j in t:
    ok = True
    num = ''
    x = 0
    for key, val in d.items():
      if j in val:
        num = key
        x = val.index(j) + 1
    if (num == prev):
      print(" ", end='')
      print(num * x, end='')
    else:
      print(num * x, end='')
    prev = num
  print("")
