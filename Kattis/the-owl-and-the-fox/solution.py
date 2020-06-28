# super slow will optimize later

for i in range(int(input())):
    n = int(input())
    x = list(map(int, str(n)))
    for j in range(n, -1, -1):
        y = list(map(int, str(j)))
        if((sum(x) - 1) == sum(y)):
            print("".join(map(str,y)))
            break 
    
