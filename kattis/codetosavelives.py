def main(T):
  for _ in range(T):
    print(' '.join(list(str(sum([int(''.join(input().split())), int(''.join(input().split()))])))))

if __name__ == '__main__':
  main(int(input()))
