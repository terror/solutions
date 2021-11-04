def main(n):
  ret = 1
  while 1:
    if n == 1:
      break
    n = (n // 2, 3 * n + 1)[n & 1]; ret += 1
  return ret

if __name__ == '__main__':
  print(main(int(input())))
