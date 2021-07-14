from math import ceil

def main():
  a, b = int(input()), int(input())
  if b % a == 0:
    print(*["*" * b // a] * a, sep="\n")
    return
  print(*["*" * ceil(b / a) for _ in range(b % a)], sep="\n")
  print(*["*" * (ceil(b / a) - 1) for _ in range(b % a, a)], sep="\n")

if __name__ == '__main__':
  main()
