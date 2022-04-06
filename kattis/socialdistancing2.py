def main(S, N):
  A = [0] * S

  for num in map(int, input().split()):
    A[num - 1] = 1

  ans = 0
  for i, v in enumerate(A):
    if not sum([v, A[(i + 1) % len(A)], A[(i - 1) % len(A)]]):
      ans += 1; A[i] = 1

  print(ans)

if __name__ == '__main__':
  main(*map(int, input().split()))
