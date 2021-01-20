while True:
    a = []
    x = int(input())
    if(x == 0):
        break
    for i in range(x):
        b = input()
        if(type(b) is str):
            a.append(b)
    a.sort(key=lambda x: x[:2])
    print(*a, sep='\n')
