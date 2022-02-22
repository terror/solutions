Sum = 0
Avg = 0
scores = []

for i in range(int(input())):
  s = int(input())
  scores.append(s)
  Sum += 0.25 * (s * (0.80**(i + 1)))

for i in range(len(scores)):
  total = 0
  _ = 0
  for j in range(len(scores)):
    if j != i:
      total += (scores[j] * (0.80**(_)))
      _ += 1
  Avg += total / 5

Avg /= len(scores)
print(Sum)
print(Avg)
