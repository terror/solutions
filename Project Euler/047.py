def main():
    n, temp = 0, []
    while len(temp) != 4:
        pf = prime_factors(n)
        print(temp)
        if len(set(pf)) == len(pf) and len(pf) == 4:
            temp.append(n)
        else:
            temp = []
        n += 1
    print(temp[0])


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


main()
