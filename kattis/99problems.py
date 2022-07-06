def main(n):
  valid = lambda x: len(x) >= 2 and x[len(x) - 2:len(x)] == '99'
  a = b = n
  a_dist = b_dist = 0
  while 1:
    if valid(str(a)): break
    a -= 1
    a_dist += 1
  while 1:
    if valid(str(b)): break
    b += 1
    b_dist += 1
  if b_dist < a_dist:
    return b
  if a_dist < b_dist:
    return a
  return ((b, a)[a > b])

if __name__ == '__main__':
  print(main(int(input())))
