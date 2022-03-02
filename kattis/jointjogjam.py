from collections import namedtuple
from math import sqrt

Range = namedtuple('Range', 'x1 y1 x2 y2')

def main(points):
  K = Range(*(points[:2] + points[4:6]))
  O = Range(*(points[2:4] + points[6:]))
  print(
    max(
      sqrt(pow(K.x1 - O.x1, 2) + pow(K.y1 - O.y1, 2)),
      sqrt(pow(K.x2 - O.x2, 2) + pow(K.y2 - O.y2, 2))
    )
  )

if __name__ == '__main__':
  main(list(map(int, input().split())))
