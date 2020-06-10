num = int(input())
while True:
    lst = list(str(num))
    Sum = 0
    for i in range(len(lst)):
        Sum += int(lst[i])
    if num % Sum == 0:
        break
    else:
        num += 1

print(num)
