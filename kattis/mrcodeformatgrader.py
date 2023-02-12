from itertools import groupby
from operator import itemgetter

n, m = map(int, input().split())

errors = list(map(int, input().split()))
correct = list(filter(lambda x: x not in errors, range(1, n + 1)))

def run(acc, data):
  for i, (a, b) in enumerate((groups := [(lambda g: (g[0], g[-1]))(list(map(itemgetter(1), g))) for _, g in groupby(enumerate(data), lambda x: x[0] - x[1])])):
    if i == len(groups) - 1: acc += (f'and {a}', f'and {a}-{b}')[a != b]
    elif i == len(groups) - 2: acc += (f'{a} ', f'{a}-{b} ')[a != b]
    else: acc += (f'{a}, ', f'{a}-{b}, ')[a != b]
  return acc

print(run('Errors: ', errors) + '\n' + run('Correct: ', correct))
