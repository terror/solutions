from collections import Counter

s = Counter(input()); m = 0

for ch in list(input()):
    if ch in s: s[ch] = 0
    if not sum(s.values()): break
    m += 1

print("WIN" if m < 10 else "LOSE")
