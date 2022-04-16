import sys

def order(line):
  ans = ''; i = 0
  while i < len(line):
    char = line[i]; count = 1; i += 1
    while i < len(line) and line[i] == line[i - 1]:
      count += 1; i += 1
    ans += f'{count}{char}'
  return ans

if __name__ == '__main__':
  print(*list(map(lambda line: order(line.strip()), sys.stdin.readlines())), sep = '\n')
