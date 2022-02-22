def main(N, M):
  for i, group in enumerate(map(int, input().split())):
    N -= group
    if N < 0:
      return M - i
  return 0

if __name__ == '__main__':
  print(main(*map(int, input().split())))
