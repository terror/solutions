def main():
  n, b, h, w = list(map(int, input().split()))
  min_price = find_min(h, n, b)
  if min_price < b:
    print(min_price)
  else:
    print("stay home")

def find_min(h, n, b):
  m = 100000000
  for i in range(h):
    p = int(input())
    avail = list(map(int, input().split()))
    for k in range(len(avail)):
      if avail[k] >= n:
        min_price = n * p
        if min_price < m:
          m = min_price
  return m

main()
