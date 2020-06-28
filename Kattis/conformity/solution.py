from collections import Counter
n = int(input())
s = [tuple(sorted(list(map(int, input().split())))) for i in range(n)]

# get frequencies
freq = Counter(s)

ans = sorted(list(freq.values()), reverse=True)
print(ans.count(ans[0])*ans[0])
