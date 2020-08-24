n = input()
while len(n) != 1:
    num = 1
    for i in n:
        if int(i) == 0:
            continue
        else:
            num *= int(i)
    n = str(num)
print(n)
