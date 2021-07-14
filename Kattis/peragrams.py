from collections import Counter

def main(s, d):
  odd = len([d[k] for k in d if d[k] & 1])
  if odd == 1 and not s == s[::-1]:
    return 0
  return max(0, odd - 1)

if __name__ == "__main__":
  (lambda x: print(main(x, Counter(x))))(list(input()))
