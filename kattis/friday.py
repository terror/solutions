def main(T):
  for _ in range(T):
    _, M = map(int, input().split())
    d = list(map(int, input().split()))

    curr = 0; count = 0
    for i in range(M):
      count += curr == 0 and d[i] >= 13
      curr = (curr + d[i]) % 7

    print(count)

if __name__ == '__main__':
  main(int(input()))
