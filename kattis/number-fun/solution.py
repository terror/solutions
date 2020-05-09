for i in range(int(input())):
    a, b, c = list(map(int, input().split()))
    if a/b == c or b/a == c or b*a == c or b-a == c or a-b == c or b+a == c:
        print("Possible")
    else:
        print("Impossible")
