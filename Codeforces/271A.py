n = str(int(input())+1)
while len(set(n)) != len(n):
    n = int(n)
    n += 1
    n = str(n)
print(n)
