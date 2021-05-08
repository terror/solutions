def main(x):
  print(x + sum([x - int(input()) for _ in range(int(input()))]))

if __name__ == '__main__':
  main(int(input()))
