for i in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    print(*s1, sep='')
    print(*s2, sep='')
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            print('*', end='')
        else:
            print('.', end='')
    print("\n")
