from collections import Counter, namedtuple

def main(n, L):
  c = Counter(L)
  A = 0
  for i in range(n):
    curr = L[i] + 1
    while curr in c and c[curr] != 0:
      c[curr] = 0
  for K in c:
    A += K * c[K]
  return A

if __name__ == '__main__':
  print(main(int(input()), sorted(list(map(int, input().split())))))
