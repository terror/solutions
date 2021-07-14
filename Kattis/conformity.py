from collections import Counter

ans = sorted(Counter([tuple(sorted(list(map(int,
                                            input().split())))) for i in range(int(input()))]).values(),
             reverse=True)
print(ans.count(ans[0]) * ans[0])
