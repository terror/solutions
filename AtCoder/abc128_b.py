from collections import defaultdict

def main():
  n = int(input())
  d = defaultdict(list)
  orig = []
  for i in range(n):
    a, b = map(str, input().split())
    b = int(b)
    d[a].append([b, i + 1])
    orig.append(a)

  x = sorted(d.keys())
  for i in x:
    if len(d[i]) > 1:
      d[i].sort(key=lambda x: x[0], reverse=True)
      for j in d[i]:
        print(j[1])
    else:
      print(orig.index(i) + 1)

if __name__ == '__main__':
  main()
