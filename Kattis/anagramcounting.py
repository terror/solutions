import sys
import math

def main():
  for word in sys.stdin:
    word = list(word.rstrip())
    n = len(set(word))

    # case 1 all distinct
    # n! is how many different ways we can arrange this word
    if n == len(word):
      print(math.factorial(n))
      continue

    # case 2 duplicates
    # take the factorial and divide it by the product
    # of the count of all dups
    s, ans = set(), 1
    for letter in word:
      if letter not in s:
        ans *= math.factorial(word.count(letter))
        s.add(letter)
    print(math.factorial(len(word)) // ans)

if __name__ == '__main__':
  main()
