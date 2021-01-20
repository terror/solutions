def main():
    n, t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if t == 1:
        seven(a)
    if t == 2:
        swag(a)
    if t == 3:
        bro(a)
    if t == 4:
        Sum(a)
    if t == 5:
        SumEven(a)
    if t == 6:
        mod(a)
    if t == 7:
        print(hop(a))


def seven(a):
    print(7)


def swag(a):
    if a[0] > a[1]:
        print("Bigger")
    elif a[0] == a[1]:
        print("Equal")
    else:
        print("Smaller")


def bro(a):
    d = a[0]
    b = a[1]
    c = a[2]
    if d > b:
        if d < c:
            median = d
        elif b > c:
            median = b
        else:
            median = c
    else:
        if d > c:
            median = d
        elif b < c:
            median = b
        else:
            median = c
    print(median)


def Sum(a):
    print(sum(a))


def SumEven(a):
    s = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            s += a[i]
    print(s)


def mod(a):
    ans = [chr(97+b % 26) for b in a]
    print(''.join(ans))


def hop(a):
    v = [False]*len(a)
    i = 0
    for _ in range(len(a)):
        if i >= len(a):
            return "Out"
        if i == len(a) - 1:
            return "Done"
        if v[i]:
            return "Cyclic"
        v[i] = True
        i = a[i]


main()
