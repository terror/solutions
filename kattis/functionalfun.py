import collections
import sys

I = collections.namedtuple('FnItem', 'input output')

def f(domain, codomain, M):
  if len(set([x.input for x in M])) != len([x.input for x in M]):
    return 'not a function'

  S = all(x in [x.output for x in M] for x in codomain)
  I = len(set([x.output for x in M])) == len([x.output for x in M])

  if S and I:
    return 'bijective'
  elif S:
    return 'surjective'
  elif I:
    return 'injective'
  else:
    return 'neither injective nor surjective'

def main(lines):
  i = 0
  while i < len(lines):
    domain   = lines[i].split()[1:]; i += 1
    codomain = lines[i].split()[1:]; i += 1

    M = []; N = int(lines[i]); i += 1; j = 0
    while j < N:
      a, b = lines[i].split(' ->')
      M.append(I(a.strip(), b.strip()))
      j += 1; i += 1

    print(f(domain, codomain, M))

if __name__ == '__main__':
  main(sys.stdin.readlines())
