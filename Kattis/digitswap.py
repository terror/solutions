s = list(input())

l = 0
r = len(s) - 1
while l <= r:
  t = s[l]
  s[l] = s[r]
  s[r] = t
  r -= 1
  l += 1

print("".join(s))
