tb = 0
lr = 0
for i in range(int(input())):
    n = list(input())
    for i in range(len(n)):
        if int(n[i]) == 0:
            if i == 0 or i == 1:
                tb += 1
            if i == 2 or i == 3:
                lr += 1
print(min(tb//2, lr//2), tb-min(tb//2, lr//2)*2, lr-min(tb//2, lr//2)*2)
