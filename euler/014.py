def main():
  mx, ans = 0, 0
  for i in range(1, 1000001):
    x = seq(i)
    if x > mx:
      mx, ans = x, i
  print(ans)

def seq(n):
  cnt = 1
  while n != 1:
    if n % 2 == 0:
      n /= 2
    else:
      n = 3 * n + 1
    cnt += 1
  return cnt

main()
