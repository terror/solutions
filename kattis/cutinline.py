def main(line):
  for _ in range(int(input())):
    OP, *data = input().split()
    if OP == "cut":
      a, b = data
      line.insert(line.index(b), a)
    else:
      line.remove(*data)
  return line

if __name__ == '__main__':
  print(*main([input() for _ in range(int(input()))]), sep = '\n')
