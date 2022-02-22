T = 0

def main():
  global T
  problems, time = map(int, input().split())
  a, b, c, T = map(int, input().split())
  times, p, pen, i = sorted([T] + [op(a, b, c) for _ in range(1, problems)]), 0, 0, 0
  while p < problems:
    time -= times[i]
    if time < 0: break
    p, pen, i = p + 1, (pen + times[i] + sum(times[:i])) % 1000000007, i + 1
  print(p, pen)

def op(a, b, c):
  global T
  T = ((a * T) + b) % c + 1
  return T

main()
