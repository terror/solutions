import sys

def main():
  start, d = int(input()), {}
  ret = [start]

  for i in sys.stdin:
    i = list(map(int, i.split()))
    if i[0] == -1: break
    for j in i[1:]:
      d[j] = i[0]

  while start in d:
    ret.append(d[start])
    start = d[start]

  print(*ret, sep=" ")

if __name__ == '__main__':
  main()
