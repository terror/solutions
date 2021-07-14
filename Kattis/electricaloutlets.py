def main():
  n = int(input())
  for i in range(n):
    x = list(map(int, input().split()))
    print(sum(x[1:]) - (x[0]) + 1)

if __name__ == '__main__':
  main()
