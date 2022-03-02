from collections import Counter

def main(N, K):
  c = Counter(list(map(int, input().split())))

  mn = int(2e5)
  for candidate in range(1, K + 1):
    mn = min(mn, c[candidate])

  ans = []
  for candidate in range(1, K + 1):
    if c[candidate] == mn:
      ans.append(candidate)

  print(len(ans))
  print(*ans)

if __name__ == '__main__':
  main(*map(int, input().split()))
