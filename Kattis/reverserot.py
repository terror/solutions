import string, sys

A = list(map(lambda x: x.upper(), string.ascii_lowercase)) + ['_', '.']

def main(L):
  for line in L:
    X = line.split()
    if len(X) == 1:
      return
    a, b = X; a, b = int(a), list(reversed(b))
    for i, v in enumerate(b):
      b[i] = A[(A.index(v) + a) % len(A)]
    print("".join(b))

if __name__ == '__main__':
  main(sys.stdin.readlines())
