from dataclasses import dataclass

@dataclass
class Pair:
  number: int
  count: int

  def __lt__(self, o):
    return self.count < o.count

def collatz(n):
  count = 0
  while n != 1:
    n = (n // 2, (3 * n) + 1)[n & 1]
    count += 1
  return count

print(max(map(lambda n: Pair(n, collatz(n)), range(1, 1000000))).number)
