from math import sqrt
from collections import namedtuple

I = namedtuple('Item', 'p l')

def M(N):
  i = N
  while 1:
    if i == pow(sqrt(i), 2):
      return i
    i += 1

def main(L):
  for item in L:
    g = []
    i = 0
    while i < len(item.p):
      g.append([*item.p[i:i + item.l]])
      i += item.l
    g = list(map(lambda x: list(reversed(x)), [*zip(*g)]))
    ans = ''
    for i in range(item.l):
      for j in range(item.l):
        if g[i][j] != '*':
          ans += g[i][j]
    print(ans)

if __name__ == '__main__':
  main(
    list(
      map(
        lambda x: I(x + '*' * (M(len(x)) - len(x)), int(sqrt(len(x + '*' * (M(len(x)) - len(x)))))),
        [input() for _ in range(int(input()))]
      )
    )
  )
