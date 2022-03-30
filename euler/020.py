from functools import lru_cache

@lru_cache
def fact(n):
  return 1 if n <= 1 else n * fact(n - 1)

print(sum(map(int, list(str(fact(100))))))
