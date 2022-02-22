d = {
  'c': [2, 3, 4, 7, 8, 9, 10],
  'd': [2, 3, 4, 7, 8, 9],
  'e': [2, 3, 4, 7, 8],
  'f': [2, 3, 4, 7],
  'g': [2, 3, 4],
  'a': [2, 3],
  'b': [2],
  'C': [3],
  'D': [1, 2, 3, 4, 7, 8, 9],
  'E': [1, 2, 3, 4, 7, 8],
  'F': [1, 2, 3, 4, 7],
  'G': [1, 2, 3, 4],
  'A': [1, 2, 3],
  'B': [1, 2]
}

def go(lst, ans):
  for x in lst:
    ans[x] += 1

def ver(a, b):
  return [x for x in a if x not in b]

def main():
  for _ in range(int(input())):
    k = list(input())
    if not k:
      print(*[0] * 10)
      continue
    ans = {i: 0 for i in range(1, 10 + 1)}
    prev = d[k[0]]
    go(prev, ans)
    for i in range(1, len(k)):
      ks = ver(d[k[i]], prev)
      go(ks, ans)
      prev = d[k[i]]
    print(*[i for i in ans.values()])

if __name__ == '__main__':
  main()
