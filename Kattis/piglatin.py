import sys

V = [
  'a',
  'e',
  'i',
  'o',
  'u',
  'y'
]

def main(l):
  for s in l:
    for i, word in enumerate(s):
      if word[0] in V:
        s[i] += "yay"
      else:
        for idx, v in enumerate(word):
          if v in V:
            s[i] = word[idx:len(word)] + word[0:idx] + "ay"
            break
    print(" ".join(s))

if __name__ == '__main__':
  main([s.split() for s in sys.stdin.readlines()])
