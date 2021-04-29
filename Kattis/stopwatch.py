times = [int(input()) for _ in range(int(input()))]; ans = 0
if len(times) & 1: print('still running'); exit()
for i in range(1, len(times), 2): ans+=times[i]-times[i-1]
print(ans)
