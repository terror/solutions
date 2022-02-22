curr = 7
for _ in range(int(input())):
  curr = max(0, curr - 1) if input() == "Skru ned!" else min(10, curr + 1)
print(curr)
