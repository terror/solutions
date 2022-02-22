n = int(input())

for _ in range(n):
  x = input()
  g, m = list(map(int, input().split()))
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  while a and b:
    if min(a) > min(b):
      b.remove(min(b))
    elif min(b) > min(a):
      a.remove(min(a))
    else:
      b.remove(min(b))

  if a:
    print("Godzilla")
  else:
    print("MechaGodzilla")
