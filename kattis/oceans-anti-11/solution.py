def main():
    n = int(input())
    for i in range(n):
        _ = int(input())
        print(list(fib(_))[_+2] % 1000000007)


def fib(n):
    a, b = 0, 1
    for _ in range(n+3):
        yield a
        a, b = b, a+b


main()
