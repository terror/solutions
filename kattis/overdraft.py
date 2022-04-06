def main(N):
  curr = ans = 0

  for _ in range(N):
    curr += int(input())
    if curr < 0:
      ans = max(ans, abs(curr))

  print(ans)

if __name__ == '__main__':
  main(int(input()))
