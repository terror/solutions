n = int(input())
for i in range(n):
  word = input()
  if len(word) > 10:
    print("{0}{1}{2}".format(word[0], len(word) - 2, word[len(word) - 1]))
  else:
    print(word)
