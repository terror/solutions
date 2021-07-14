b, br, bs, a, As = list(map(int, input().split()))

tot = 0
while tot <= (abs(br - b) * bs):
  tot += As
  a += 1

print(a)
