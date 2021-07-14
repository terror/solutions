for _ in range(int(input())):
  n = list(map(int, input().split()))[1:]
  print("{:.3f}%".format((sum([1 for i in n if i > sum(n) / len(n)]) / len(n)) * 100))
