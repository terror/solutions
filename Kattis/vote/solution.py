t = int(input())

for _ in range(t):
    n = int(input())
    v = [int(input()) for i in range(n)]
    tot, v2, mx = sum(v)/2, sorted(v, reverse=True), v.index(max(v))

    if(v2[0] == v2[1]):
        print("no winner")
    else:
        if(v[mx] > tot):
            print("majority winner", mx+1)
        else:
            print("minority winner", mx+1)
