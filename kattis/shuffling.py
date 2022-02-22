import math

def main():
  n, op = map(str, input().split())

  state = [i for i in range(1, int(n) + 1)]

  cnt = 1

  if op == "out":
    x = go(shuffle_out(state))
    while x != state:
      cnt += 1
      x = go(shuffle_out(x))
    return cnt

  x = go(shuffle_in(state))
  while x != state:
    cnt += 1
    x = go(shuffle_in(x))

  return cnt

def shuffle_out(arr):
  if len(arr) & 1:
    a = math.ceil(len(arr) / 2)
    return list(zip(arr[:a], arr[a:])) + [arr[a - 1]]

  mid = len(arr) // 2
  return list(zip(arr[:mid], arr[mid:]))

def shuffle_in(arr):
  if len(arr) & 1:
    a = math.floor(len(arr) / 2)
    return list(zip(arr[a:], arr[:a])) + [arr[-1]]

  mid = len(arr) // 2
  return list(zip(arr[mid:], arr[:mid]))

def go(arr):
  new = []
  for i in arr:
    if isinstance(i, tuple):
      for j in i:
        new.append(j)
    else:
      new.append(i)
  return new

if __name__ == '__main__':
  print(main())
