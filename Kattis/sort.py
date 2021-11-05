from collections import Counter
from functools import cmp_to_key

def main(L):
  c = Counter(L)

  def cmp(a, b):
    if c[a] > c[b]:
      return -1
    elif c[a] < c[b]:
      return 1
    else:
      return -1 if L.index(a) < L.index(b) else 1
    return 0

  return sorted(L, key=cmp_to_key(cmp))

if __name__ == '__main__':
  _ = map(int, input().split())
  print(*main(list(map(int, input().split()))))
