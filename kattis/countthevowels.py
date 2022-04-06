def main(s):
  a = 0; v = ['a', 'e', 'i', 'o', 'u']
  for c in s:
    a += c.lower() in v
  print(a)

if __name__ == '__main__':
  main(input())
