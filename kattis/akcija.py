n = int(input())
books = sorted([int(input()) for i in range(n)], reverse=True)
s = 0
for i in range(len(books)):
  if i % 3 != 2:
    s += books[i]
print(s)
