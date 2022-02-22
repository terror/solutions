import sys
from math import sqrt

def dis(x, y):
  return sqrt(sum([(a - b)**2 for a, b in zip(x, y)]))

def main():
  for i, line in enumerate(sys.stdin):
    if not i:
      a, b, c, d = map(float, line.split())
    else:
      x, y = map(float, line.split())
      if 2 * dis([a, b], [x, y]) < dis([c, d], [x, y]):
        print('The gopher can escape through the hole at ({:.3f},{:.3f}).'.format(x, y))
        exit()
  print('The gopher cannot escape.')

if __name__ == "__main__":
  main()
