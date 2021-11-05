*heights, h1, h2 = list(map(int, input().split()))

ans1 = []
ans2 = []
for i in range(len(heights)):
  for j in range(i + 1, len(heights)):
    for k in range(j + 1, len(heights)):
      if heights[i] + heights[j] + heights[k] == h1 and not any(
        x in ans1 for x in [heights[i], heights[j], heights[k]]
      ):
        ans1.extend([heights[i], heights[j], heights[k]])
      if heights[i] + heights[j] + heights[k] == h2 and not any(
        x in ans2 for x in [heights[i], heights[j], heights[k]]
      ):
        ans2.extend([heights[i], heights[j], heights[k]])
print(*sorted(ans1, reverse=True), *sorted(ans2, reverse=True))
