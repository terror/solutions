OP = {'*': lambda x, y: x * y, '+': lambda x, y: x + y, '-': lambda x, y: x - y, '/': lambda x, y: x // y}

def main(a, b, c, d):
  ans = []

  for i in OP:
    for j in OP:
      try:
        if OP[i](a, b) == OP[j](c, d):
          ans.append(f'{a} {i} {b} = {c} {j} {d}')
      except:
        continue

  if not ans:
    print('problems ahead')
    return

  print(*ans, sep="\n")

if __name__ == '__main__':
  main(*map(int, input().split()))
