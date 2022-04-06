from collections import Counter

def main(N, M):
  friends = Counter()

  for _ in range(M):
    a, b = map(int, input().split())
    friends[a] += 1; friends[b] += 1

  print(*[friends[i] - i for i in range(1, N + 1)])

if __name__ == '__main__':
  main(*map(int, input().split()))
