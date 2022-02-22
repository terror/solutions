def go(o, a, b):
  if o == '+':
    return a + b
  return a * b

def main():
  a, o, b = int(input()), input(), int(input())
  return go(o, a, b)

if __name__ == '__main__':
  print(main())
