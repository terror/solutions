def main():
  n = int(input())
  d = [0] * (n * 4)
  for i in range(n * 4):
    s = input().lower().split()
    d[i] = syl(s).lower()

  for i in range(0, n * 4, 4):
    print(solve(d[i:i + 4]))

def syl(s):
  v = 'aeiou'
  for i in s[-1][::-1]:
    if i in v:
      return "".join(s[-1][s[-1].rindex(i):])
  return "".join(s[-1])

def solve(d):
  if len(set(d)) == 1:
    return "perfect"
  if d[0] == d[1] and d[2] == d[3]:
    return "even"
  if d[0] == d[2] and d[1] == d[3]:
    return "cross"
  if d[0] == d[3] and d[1] == d[2]:
    return "shell"
  return "free"

main()
