import sys, collections

def main(a, b):
  for _ in range(int(input())):
    name, *items = map(str, input().split())
    a[name] = items[1:]

  for l in sys.stdin.readlines():
    for k in a:
      b[k] += sum([l.split().count(c) for c in a[k]])

  print(*sorted([k for k, v in b.items() if v == max(b.values())]), sep="\n")

if __name__ == '__main__':
  main(collections.defaultdict(list), collections.Counter())
