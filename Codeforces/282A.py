tot = 0
for i in range(int(input())):
    a = input()
    if "+" in a:
        tot += 1
    else:
        tot -= 1
print(tot)
