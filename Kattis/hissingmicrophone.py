def x(y):
    for i in range(1, len(y)):
        if y[i] == 's' and y[i-1] == 's': return "hiss"
    return "no hiss"

print(x(input()))
