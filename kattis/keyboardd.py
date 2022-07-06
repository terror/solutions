from collections import Counter

print(''.join((lambda a, b: list(map(lambda e: e[0], filter(lambda e: e[1] * 2 == b[e[0]], a.items()))))(Counter(input()), Counter(input()))))
