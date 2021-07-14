def main():
  for i in range(int(input())):
    k, n, b = list(map(int, input().split()))
    ans = solve(numberToBase(b, n))
    print("{0} {1}".format(k, ans))

def numberToBase(b, n):
  digits = []
  while b:
    digits.append(b % n)
    b //= n
  return digits

def solve(n):
  Sum = 0
  for i in range(len(n)):
    Sum += n[i]**2
  return Sum

main()
