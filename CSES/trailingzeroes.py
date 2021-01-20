from math import factorial


def main():
    n = str(factorial(int(input())))[::-1]
    ans = 0
    for i in n:
        if i == '0':
            ans += 1
        else:
            break
    print(ans)


main()
