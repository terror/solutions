from math import sqrt

N = 600851475143

print(max(list(filter(lambda x: N % x == 0 and all(map(lambda i: x % i, range(2, int(sqrt(x)) + 1))), range(2, int(sqrt(N) + 1))))))
