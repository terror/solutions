from math import sqrt

prime = lambda x: all(map(lambda i: x % i, range(2, int(sqrt(x)) + 1)))

print(sum(map(lambda x: x * prime(x), range(2, 2_000_000))))
