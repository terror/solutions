def main():
  a, b, c = list(map(int, input().split()))
  print(solve(a, b, c))

def solve(a, b, c):
  if a + b == c:
    return "{0}+{1}={2}".format(a, b, c)
  elif a - b == c:
    return "{0}-{1}={2}".format(a, b, c)
  elif a / b == c:
    return "{0}/{1}={2}".format(a, b, c)
  elif a * b == c:
    return "{0}*{1}={2}".format(a, b, c)
  if b + c == a:
    return "{0}={1}+{2}".format(a, b, c)
  elif b - c == a:
    return "{0}={1}-{2}".format(a, b, c)
  elif b / c == a:
    return "{0}={1}/{2}".format(a, b, c)
  elif b * a == c:
    return "{0}={1}*{2}".format(a, b, c)

main()
