from functools import reduce
from itertools import combinations

CARD_SIZE = 4
ROWS = 4
SET_SIZE = 3

def is_set(subset):
  for i in range(CARD_SIZE):
    if len(set([subset[0][i], subset[1][i], subset[2][i]])) == 2:
      return False
  return True

def main(sets):
  if not sets:
    print('no sets')
  else:
    for set in sets:
      print(*set)

if __name__ == '__main__':
  cards = reduce(lambda x, y: x + y, [input().split() for _ in range(ROWS)])

  for i in range(len(cards)):
    cards[i] += str(i + 1)

  main((
    lambda cards: sorted(
      list(
        map(
          lambda subset:
          sorted(list(map(lambda card: int(card[CARD_SIZE:]), subset))),
          filter(lambda subset: is_set(subset), combinations(cards, SET_SIZE))
        )
      )
    )
  )(cards))
