from collections import Counter
s, a, ans = input(), list("abcdefghijklmnopqrstuvwxyz"), 0

for k, v in Counter(s).items():
    ans += (a.index(k)+1)*v

print(ans)
