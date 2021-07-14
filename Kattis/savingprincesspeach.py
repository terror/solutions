N, Y = list(map(int, input().split()))

tot = [i for i in range(N)]
diff = []
for i in range(Y):
  diff.append(int(input()))

totdiff = sorted([i for i in tot if i not in diff])

for i in range(len(totdiff)):
  print(totdiff[i])

print("Mario got {0} of the dangerous obstacles.".format(abs(len(totdiff) - len(tot))))
