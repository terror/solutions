for i in range(int(input())):
    k, n = list(map(int, input().split()))
    print("{0} {1}".format(k, sum(range(n)) + (n*2)))
