import math
import itertools


def main():
    Sum = 0
    for i in range(2000000):
        if is_prime(i):
            Sum += i
    print(Sum)


def is_prime(n):
    return n > 1 and all(n % i for i in itertools.islice(itertools.count(2), int(math.sqrt(n)-1)))


main()
