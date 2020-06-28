def compute_k(n, d):
    for i in range(n[0]):
        if d[i] <= n[1]:
            return "It hadn't snowed this early in {0} years!".format(i)
    return "It had never snowed this early!"


n = list(map(int, input().split()))
d = list(map(int, input().split()))
print(compute_k(n, d))
