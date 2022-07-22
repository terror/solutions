from functools import lru_cache

@lru_cache
def fib(n):
  return n if n < 2 else fib(n - 1) + fib(n - 2)

i = 0
while len(str(fib(i))) < 1000:
  i += 1

print(i)
