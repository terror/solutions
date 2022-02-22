def main():
  n, t = map(int, input().split())
  a = list(map(int, input().split()))

  {
    1: lambda x: print(7),
    2: lambda x: print("Bigger" * (x[0] > x[1]) + "Equal" * (x[0] == x[1]) or "Smaller"),
    3: lambda x: print(sorted([x[0], x[1], x[2]])[1]),
    4: lambda x: print(sum(x)),
    5: lambda x: print(sum([i for i in x if i & 1 == 0])),
    6: lambda x: print(''.join([chr(97 + i % 26) for i in x])),
    7: lambda x: print(seven(x))
  }[t](a)

def seven(a):
  v, i = [False] * len(a), 0
  for _ in range(len(a)):
    if i >= len(a): return "Out"
    if i == len(a) - 1: return "Done"
    if v[i]: return "Cyclic"
    v[i] = True
    i = a[i]

if __name__ == "__main__":
  main()
