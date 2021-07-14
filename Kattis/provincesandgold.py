g, s, c = list(map(int, input().split()))
power = g * 3 + s * 2 + c

ans = []
if power > 7:
  ans.append("Province")
elif power > 4:
  ans.append("Duchy")
elif power > 1:
  ans.append("Estate")
if power > 5:
  ans.append("Gold")
elif power > 2:
  ans.append("Silver")
else:
  ans.append("Copper")

if len(ans) > 1:
  print("{0} or {1}".format(ans[0], ans[1]))
else:
  print(*ans)
