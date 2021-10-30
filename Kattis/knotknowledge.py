if __name__ == '__main__':
  n = int(input());
  print(*(set(map(int, input().split())) - set(map(int, input().split()))))
