def main():
    ans = 1
    for n in range(1, 501):
        ans += f(n)
    print(ans)


def f(n):
    return 4*(2*n+1)**2 - (12*n)


if __name__ == '__main__':
    main()
