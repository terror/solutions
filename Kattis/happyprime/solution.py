import itertools
import math


def main():
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(a, b, "YES" if is_happy(b) and is_prime(b) else "NO")


def is_happy(n):
    s = set()
    while True:
        num = n
        Sum = 0
        while num != 0:
            Sum += (num % 10)**2
            num //= 10
        n = Sum
        if Sum in s:
            return False
        else:
            s.add(Sum)
        if Sum == 1:
            break
    return True


def is_prime(n):
    return n > 1 and all(n % i for i in itertools.islice(itertools.count(2), int(math.sqrt(n)-1)))


main()
