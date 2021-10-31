import string

A = list(map(lambda c: c.upper(), string.ascii_lowercase))

def main(c, K):
  ans = ''
  for i in range(len(c)):
    # ACM -> SEN -> ...
    _ = A[(A.index(c[i]) - A.index(K[i % len(K)])) % len(A)]
    K[i % len(K)] = _; ans += _
  return ans

if __name__ == '__main__':
  print(main(input(), list(input())))
