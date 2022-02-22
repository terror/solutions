import sys
import math
import itertools

def main():
  for i in sys.stdin:
    i = int(i)
    if i == 0:
      break
    if is_prime(i):
      print(get_prime(2 * i))
    else:
      print(get_prime(2 * i), "({} is not prime)".format(i))

def is_prime(n):
  return n > 1 and all(n % i for i in itertools.islice(itertools.count(2), int(math.sqrt(n) - 1)))

def get_prime(i):
  while not is_prime(i):
    i += 1
  return i

if __name__ == '__main__':
  main()
