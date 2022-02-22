n = list(map(int, input().split()))
rc = n[0] - n[1]
ans = format(rc * rc * 100 / (n[0] * n[0]), '.6f')
print(ans)
