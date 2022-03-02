def main(candidates, correct):
  mx = 0; ans = 1
  for i, candidate in enumerate(candidates):
    common = 0
    for j in range(len(candidate)):
      common += candidate[j] == correct[j]
    if common > mx:
      mx, ans = common, i + 1
  print(ans)

if __name__ == '__main__':
  main(
    *(lambda N, M: ([input().split() for _ in range(N)],
     (lambda M: list(map(lambda x: 'fizz' * (x % 3 == 0) + 'buzz' * (x % 5 == 0) or str(x), range(1, M + 1))))(M)))
     (*map(int, input().split()))
  )
