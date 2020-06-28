from collections import Counter
s = (input())

ans = ' '.join([s[i:i+len(list(s)) // 3]
                for i in range(0, len(s), len(list(s)) // 3)])
counts = Counter(ans.split())

for key, val in counts.items():
    if val > 1:
        print(key)
