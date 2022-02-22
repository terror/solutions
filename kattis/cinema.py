def main(N, M):
  ans = 0
  for i, group in enumerate(map(int, input().split())):
    if N - group < 0:
      ans += 1
    else:
      N -= group
  return ans

if __name__ == '__main__':
  print(main(*map(int, input().split())))
