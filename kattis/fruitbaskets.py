import itertools, math

print((
  lambda N, L: sum([
    sum(
      map(
        lambda i: sum(
          list(
            map(
              sum,
              filter(lambda c: sum(c) >= 200, itertools.combinations(L, i))
            )
          )
        ),
        range(1, min(4, N + 1))
      )
    ),
    sum(
      map(
        lambda i: sum(list(map(lambda x: math.comb(N - 1, i - 1) * x, L))),
        range(4, N + 1)
      )
    )
  ])
)(int(input()), list(map(int, input().split()))))
