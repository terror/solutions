def main(a, b):
  cards = list(input())

  cards[cards.index('A')] = a
  cards[cards.index('A')] = b

  if cards[-1] == 'B' and cards[-2] == 'B':
    return ([-1], [8, 9])[b == 7]

  prev = 0; prev_idx = 0; ans = []
  for i, v in enumerate(cards):
    if v != 'B':
      count = cards[prev_idx:i].count('B')
      if count == 0:
        prev = int(v)
        continue
      if count != int(v) - prev - 1:
        return [-1]
      else:
        for i in range(1, count + 1):
          ans.append(int(v) - i)
        ans.sort()
      prev = int(v); prev_idx = i

  if cards[-1] == 'B':
    if b != 8:
      return [-1]
    ans.append(9)

  return ans

if __name__ == '__main__':
  print(*main(*map(int, input().split())))
