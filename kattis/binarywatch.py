def run(number):
  ans = []
  for digit in number:
    start = 8
    row = ''
    digit = int(digit)
    while digit:
      if start > digit:
        start //= 2
        row += '.'
        continue
      digit -= start
      row += '*'
      start //= 2
    while len(row) != 4:
      row += '.'
    ans.append(list(row))
  return ans

def out(matrix):
  for row in matrix[:2]:
    row.insert(2, ' ')
    print(*row)
  for row in matrix[2:]:
    row.insert(2, ' ')
    print(*row)

if __name__ == '__main__':
  out(list(map(lambda x: list(x), zip(*run(input())))))
