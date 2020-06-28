n = int(input())
t, k = list(map(float, input().split()))
tot = 0
for i in range(n - 1):
    t1, k1 = list(map(float, input().split()))
    tot += ((k+k1)/2)*(t1-t)/1000
    t = t1
    k = k1
print(tot)
