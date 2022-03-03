R = 4

class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def dist(self, o):
    return abs(self.x - o.x) + abs(self.y - o.y)

class Grid:
  def __init__(self, inner):
    self.inner = inner

  def get(self, i, j):
    return self.inner[i][j]

  def find(self, target):
    for i in range(R):
      for j in range(R):
        if self.inner[i][j] == target:
          return Position(i, j)
    return None

def main(have, want):
  ans = 0
  for i in range(R):
    for j in range(R):
      if want.get(i, j) == '.':
        continue
      ans += have.find(want.get(i, j)).dist(Position(i, j))
  print(ans)

if __name__ == '__main__':
  main(
    have = Grid([list(input()) for _ in range(R)]),
    want = Grid([['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', '.']])
  )
